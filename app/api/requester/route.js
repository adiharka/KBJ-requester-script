export const dynamic = 'force-dynamic'; // static by default, unless reading the request

function randomizeSlug() {
    return Math.random().toString(36).substring(2);
}

export async function GET(request) {
    const url = 'https://dummyjson.com/users/'
    // get request to the url
    const response = await fetch(url + randomizeSlug());
    // get the json data
    const data = await response.json();
    // return the data
    return new Response(JSON.stringify(data));
}