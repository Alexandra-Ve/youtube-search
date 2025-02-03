import db from './db';

export const fetchAllVideos = async ({search = ''} : {search:string}) => {

    return db.youtube_videos.findMany({
        where: {
            OR: [
                {title: {contains: search, mode: 'insensitive'}},
                {description: {contains: search, mode: 'insensitive'}}
            ]
        }
    });
}

export const fetchChannelByID = async ({ channelID }: { channelID: string }) => {
    const channel = await db.youtube_channels.findUnique({
        where: { channel_id: channelID },
    });
    return channel;
};