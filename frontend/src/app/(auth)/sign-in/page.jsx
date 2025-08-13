"use client";
import { useState } from "react";
import axios from "axios";

export default function Signin() {
    const [form, setForm] = useState({ email: "", password: "" });
    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage("");

        try {
            const response = await axios.post("/api/signin", form);
            const token = response.data.token;

            // Store token locally (optional)
            localStorage.setItem("token", token);

            setMessage("✅ Login successful!");
        } catch (error) {
            if (error.response) {
                setMessage("❌ " + error.response.data.message);
            } else {
                setMessage("❌ Server error");
            }
        }
    };

    return (
        <div style={{ maxWidth: "400px", margin: "auto" }}>
            <h2>Sign In</h2>
            <form onSubmit={handleSubmit}>
                <input
                    name="email"
                    type="email"
                    placeholder="Email"
                    required
                    onChange={handleChange}
                    value={form.email}
                />
                <br />
                <br />
                <input
                    name="password"
                    type="password"
                    placeholder="Password"
                    required
                    onChange={handleChange}
                    value={form.password}
                />
                <br />
                <br />
                <button type="submit">Login</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}
