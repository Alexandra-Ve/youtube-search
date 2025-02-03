
import Videos from "@/components/videos/videos";
import {fetchAllVideos} from "../../utils/actions";
import {Suspense} from "react";

async function HomePage({searchParams}: {searchParams: Promise<any>}) {
    // @ts-ignore
    const search = searchParams?.search || '';

    // @ts-ignore
    const videos = await fetchAllVideos( {search});

    return (
        <Suspense fallback={<div>loading...</div>}>
            < Videos videos={videos} />
        </Suspense>

    )
}

export default HomePage