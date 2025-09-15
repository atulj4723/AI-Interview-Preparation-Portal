import Interview from "@/components/Interview";
import React, { Suspense } from "react";

const page = async ({ params }) => {
    const { id } = await params;
    return (
        <Suspense fallback={<div className="animate-pulse">loading ....</div>}>
            <Interview id={id} />
        </Suspense>
    );
};

export default page;
