import {youtube_channels, youtube_videos} from "@prisma/client";
import { Card, CardContent } from "@/components/ui/card";
import SingleVideo from "@/components/singleVideo/singleVideo";
import {fetchChannelByID} from "../../../utils/actions";

export default async function Videos({ videos }: { videos: youtube_videos[] }) {

    return (
        <div className="pt-12 grid gap-4 lg:grid-cols-4">
            {videos.map(async (video) => {

                const channel: youtube_channels | null = await fetchChannelByID({ channelID: video.channel_id })
                return (
                    <article className="group relative" key={video.video_id}>
                        <Card className="transform group-hover:shadow-xl transition-shadow duration-500 h-full max-h-max">
                            <CardContent className="p-4">
                                <SingleVideo video={video} channelName={channel?.channel_name || ''} channelSubscribers={channel?.subscribers || 0} />
                            </CardContent>
                        </Card>
                    </article>
                );
            })}
        </div>
    );
}
