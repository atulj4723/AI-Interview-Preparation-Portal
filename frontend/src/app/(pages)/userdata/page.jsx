"use client";

import { useState } from "react";
import axios from "axios";
import { useUser } from "@/utils/UserData";

export default function ProfileUpload() {
    const [file, setFile] = useState(null);
    const { user } = useUser();
    console.log(user);
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            alert("Please select a file");
            return;
        }

        const data = new FormData();
        data.append("file", file);
        data.append("user_id", user._id);
        try {
            const res = await axios.post(
                `${process.env.NEXT_PUBLIC_BASE_URL}/profile`,
                data,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );
            console.log("Response:", res.data);
        } catch (err) {
            console.error("Error uploading profile:", err);
        }
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="flex flex-col gap-4 w-[300px] p-4 border rounded-lg">
            <input type="file" onChange={handleFileChange} />
            <button
                type="submit"
                className="bg-blue-500 text-white px-4 py-2 rounded-md">
                Upload
            </button>
        </form>
    );
}
