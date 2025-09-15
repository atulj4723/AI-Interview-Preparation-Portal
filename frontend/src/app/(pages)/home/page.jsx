export default function Home() {
    return (
        <div className="bg-gray-950 w-[100vw] h-[100vh] flex flex-col">
            <nav className=" w-screen h-[7vh] flex items-center font-serif nounderline text-purple-500 font-semibold hover:underline decoration-3 decoration-sky-600">
                TechinterviewBuddy
            </nav>
            <div className="h-[93vh] w-full flex">
                <div className="h-full w-6/12  flex flex-col items-center justify-center">
                    <p className=" text-5xl text-white font-sans font-bold mx-5">
                        AI-Powered Interview Preparation Portal
                    </p>
                    <p className="text-gray-600 font-sans font-semibold mx-5">
                        Practice mock interviews with voice, get instant
                        feedback, and track your score.
                    </p>
                    <button className="bg-purple-500 rounded-xl font-semibold font-sansmy-15 transition hover:-translate-y-1 hover:scale-110 hover:bg-purple-400 ease-in w-[250px] h-[40px] my-15">
                        Start Interview
                    </button>
                </div>
                <div className="h-full w-6/12 "></div>
            </div>
        </div>
    );
}
