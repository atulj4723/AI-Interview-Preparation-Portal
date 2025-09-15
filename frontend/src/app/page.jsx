import React from "react";

const page = () => {
    return (
        <>
            <div className="absolute inset-0   bg-cover bg-center" style={{ backgroundImage: "url('/background-intro1.jpg')" }}>
                <div className="absolute inset-0 bg-black/50"></div>
            </div>

            <div className="relative z-10 flex flex-col h-full">
                <div className="flex justify-between items-center px-4 sm:px-6 pt-4">
                    <h1 className="text-xl sm:text-2xl font-bold text-white">
                        Interview
                    </h1>
                    <a
                        href="#"
                        className="text-xs sm:text-sm font-semibold text-white bg-purple-600 hover:bg-purple-700 px-3 sm:px-4 py-1.5 sm:py-2 rounded-lg transition-colors">
                        Introduction
                    </a>
                </div>

                <div className="flex flex-col justify-center flex-1 px-4 sm:px-6 md:px-20 text-center sm:text-left pt-30">
                    <h1 className="text-3xl sm:text-4xl md:text-6xl font-extrabold text-white leading-tight mb-4 sm:mb-6">
                        Let's Start Your Journey
                    </h1>

                    <p className="text-base sm:text-lg md:text-xl text-gray-200 max-w-2xl mx-auto sm:mx-0 mb-8 sm:mb-10">
                        Unlock Your Potential, Empower Your Career
                    </p>
                    <div>
                        <a
                            href="#"
                            className="inline-block bg-purple-600 text-white font-bold text-lg px-8 py-4 rounded-full animate-bounce shadow-xl hover:bg-purple-700 transition-all transform hover:scale-105">
                            Start Now
                        </a>
                    </div>
                </div>
            </div>
        </>
    );
};

export default page;
