import { youtube_videos} from "@prisma/client";
import Image from 'next/image';

async function SingleVideo({ video, channelName, channelSubscribers}: { video: youtube_videos, channelName: string, channelSubscribers: number| bigint}) {

    return (
        <>
            <div className='relative h-64 rounded overflow-hidden'>
                <Image src={video.thumbnail_url} alt={video.title} fill sizes='(max-width:475px) 100vw' priority
                       className='rounded w-full object-cover transform group-hover:scale-110 transition-transform duration-500'/>
            </div>
            <div className='mt-4 text-left'>
                <h4 className='text-lg capitalize '>{video.title}</h4>
                <div className='grid grid-cols-2 pt-4'>
                    <p className='text-sm text-muted-foreground text-left'> {video.views} views</p>
                    <p className='text-sm text-muted-foreground text-right'> {video.published_at.toDateString()} </p>
                </div>
                <p className='text-sm text-muted-foreground'>@ {channelName} *  {channelSubscribers}subs</p> {/* ✅ Displays the channel name */}
            </div>
        </>
    );
}

export default SingleVideo;
