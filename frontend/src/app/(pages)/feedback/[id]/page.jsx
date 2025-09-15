import FeedBack from "@/components/FeedBack";
import React, { Suspense } from "react";

const page = async ({ params }) => {
    const { id } = await params;
    return (
        <Suspense fallback={<div className="animate-pulse">loading ....</div>}>
            <FeedBack id={id}/>
        </Suspense>
    );
};

export default page;
