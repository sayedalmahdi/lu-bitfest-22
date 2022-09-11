export const handle = async ({ event, resolve })=>{
  console.log("H");
  console.log(event.url.pathname);
    // if (event.url.pathname === "/log"){
    //    return Response.redirect(`${event.url.origin}/login`,301)
    // }
    return await resolve(event);
  }