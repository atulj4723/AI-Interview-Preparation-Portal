"use client";

import axios from "axios";
import { useState } from "react";

const interview = () => {
    const [conversation, setConversation] = useState([]);
    const [input, setInput] = useState("");
    const [lastAIResponse, setLastAIResponse] = useState("");

    const handleSend = async () => {
        const newMessage = { role: "user", parts: [{ text: input }] };
        const updatedConversation = [...conversation, newMessage];
        setConversation(updatedConversation);
        setInput("");

        try {
            const res = await axios.post(
                `${process.env.NEXT_PUBLIC_BASE_URL}/interview-stimulation`,
                {
                    jobDescription: "WEB Developer",
                    roundName: "technical round",
                    user_id: "12345",
                    questions: [
                        {
                            question:
                                "Describe your experience with React and Next.js, and how you've used them in your projects.",
                            answer: "I have experience using React for building user interfaces and Next.js for server-side rendering and improved performance. For example, in the FitBuddy project, I used React for the front-end components, and in the AI Recruiter project, I utilized Next.js for its SSR capabilities.",
                        },
                        {
                            question:
                                "Explain your approach to designing and implementing RESTful APIs using Node.js and Express.",
                            answer: "When designing RESTful APIs, I focus on creating well-defined endpoints that follow REST principles. I use Node.js with Express to handle routing, middleware, and request processing. I ensure proper error handling, authentication, and data validation for secure and efficient API development.",
                        },
                        {
                            question:
                                "Discuss your experience with MongoDB and MySQL, including schema design, querying, and optimization techniques.",
                            answer: "I have worked with MongoDB, a NoSQL database, in projects like ChatApp, where I designed the schema to efficiently store and retrieve real-time messages. I've also used MySQL, a relational database, and understand schema design principles and query optimization techniques like indexing to improve performance.",
                        },
                        {
                            question:
                                "How have you integrated AI/ML techniques into your web development projects, and what tools or libraries have you used?",
                            answer: "I've integrated AI/ML into web development through projects like the AI Recruiter and JARVIS AI Assistant. I use libraries such as Flask for creating APIs to serve AI models, Next.js for front-end integration, and NLP techniques for resume parsing. I've also worked with the Gemini API for AI assistant functionalities.",
                        },
                        {
                            question:
                                "Describe your experience with Git and Docker, and how you use them in your development workflow.",
                            answer: "I use Git for version control, managing code changes, and collaborating with others. I utilize Docker for containerizing applications, ensuring consistent environments across development, testing, and deployment. This helps streamline the deployment process and avoid environment-related issues.",
                        },
                    ],
                    content: updatedConversation,
                    resume: "Atul Mohan Jadhav, Karad, Maharashtra | Email: atulj9537@gmail.com | Phone: +91-7887477957 | LinkedIn: linkedin.com/in/atulj | Summary: Final year Computer Science and Engineering student with experience in full-stack web development, AI-powered applications, and database management. Skilled in React, Next.js, Node.js, Python, Flask, MongoDB, and SQL. Strong problem-solving and debugging skills. Projects: ChatApp – real-time messaging application using Node.js, Socket.io, and MongoDB; AI Recruiter – intelligent recruitment assistant using Flask, Next.js, and NLP resume parsing; JARVIS AI Assistant – CLI and desktop AI assistant with memory, tool-use, and web integration using Python and Gemini API; FitBuddy – fitness tracker web app with diet and workout modules using React and Express. Education: B.E. in Computer Science and Engineering, 2025. Skills: React, Next.js, Node.js, Python, Flask, MongoDB, MySQL, REST APIs, Git, Docker, AI/ML basics. Achievements: Google AI Pro Student Pack access, developed multiple AI-powered apps, and open-source contributions. Interests: AI agents, system design, and cloud deployment.",
                }
            );
            setConversation((prev) => [...prev, { role: "model", parts: [{ text: res.data.data }] }]);
            setLastAIResponse(res.data.data);
        } catch (e) {
            console.log(e);
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
                    <p className="text-lg">
                        {
                            lastAIResponse 
                        }
                    </p>
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
export default interview;
