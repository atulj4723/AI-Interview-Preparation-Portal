"use client";
import { useUser } from "@/utils/UserData";
import axios from "axios";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

const Interview = ({ id }) => {
    const [conversation, setConversation] = useState([]);
    const [input, setInput] = useState("");
    const [interview, setInterview] = useState({});
    const { resume } = useUser();
    const [lastAIResponse, setLastAIResponse] = useState("");
    const router = useRouter();
    useEffect(() => {
        try {
            const fetchData = async () => {
                const res = await axios.get(
                    `${process.env.NEXT_PUBLIC_BASE_URL}/interview/specific/${id}`
                );
                setInterview(res.data.data);
            };
            fetchData();
        } catch (e) {
            console.log(e);
        }
    }, []);
    const handleSend = async () => {
        if (!input.trim()) return;

        const newMessage = { role: "user", parts: [{ text: input }] };
        const updatedConversation = [...conversation, newMessage];

        setConversation(updatedConversation);
        setInput("");

        try {
            const res = await axios.post(
                `${process.env.NEXT_PUBLIC_BASE_URL}/interview-stimulation`,
                {
                    jobDescription: interview.jobDescription,
                    roundName: interview.roundName,
                    user_id: interview.user_id,
                    questions: interview.questions,
                    content: updatedConversation,
                    resume,
                }
            );

            const aiResponse = {
                role: "model",
                parts: [{ text: res.data.data }],
            };

            const finalConversation = [...updatedConversation, aiResponse];
            setConversation(finalConversation);
            setLastAIResponse(res.data.data);

            if (res.data.data.includes("quit")) {
                await axios.post(
                    `${process.env.NEXT_PUBLIC_BASE_URL}/conversation`,
                    {
                        user_id: interview.user_id,
                        interview_id: interview._id,
                        conversations: finalConversation,
                    }
                );

                const feedback = await axios.post(
                    `${process.env.NEXT_PUBLIC_BASE_URL}/generate-feedback`,
                    {
                        resume,
                        questionAnswer: interview.questions,
                        userAnswer: finalConversation,
                        jobDescription: interview.jobDescription,
                        roundName: interview.roundName,
                    }
                );

                const feedbackSave = await axios.post(
                    `${process.env.NEXT_PUBLIC_BASE_URL}/feedback`,
                    {
                        feedback: feedback.data.data,
                        interviewId: interview._id,
                    }
                );
                router.push(`/feedback/${feedbackSave.data.data._id}`);
            }
        } catch (e) {
            console.error("Interview error:", e);
        }
    };

    return (
        <div className="w-full h-screen bg-gray-900 ">
            <div className="h-[70vh] w-full flex">
                {/* this is left */}
                <div className="h-[70vh] w-6/12  flex items-center justify-center">
                    <div className="h-[60vh] w-[45vw]  border-2  border-purple-500 rounded-xl backdrop-blur-none  bg-white/10"></div>
                </div>
                {/* this is right */}
                <div className="h-[70vh] w-6/12 flex items-center justify-center">
                    <div className="h-[60vh] w-[45vw] border-2  border-purple-500 rounded-xl backdrop-blur-none  bg-white/10 "></div>
                </div>
            </div>
            <div className="h-[30vh] w-full flex items-center justify-center">
                <div className="h-[25vh] w-[97vw] border-2 flex flex-col border-purple-500 rounded-xl backdrop-blur-none bg-white/10 p-4">
                    <p className="text-lg">{lastAIResponse}</p>
                    <div className="w-full flex justify-between gap-4 mt-auto">
                        <input
                            type="text"
                            placeholder="Any question"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            className="rounded-xl backdrop-blur-none  bg-white/10 w-[70vw] h-[5vh] mt-auto p-4"
                        />
                        <button
                            className="bg-purple-500 p-1 rounded px-2"
                            onClick={handleSend}>
                            Send
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};
export default Interview;
