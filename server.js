const handler = require("serve-handler");
const http = require("http");
const server = http.createServer((request, response) => {
  console.log(request.url);
  if (request.url == "/install") {
    response.writeHead(302, { Location: "/install/start" });
    response.end();
    return 0;
  } else if (request.url == "/install/start") {
    request.url = request.url.replace("/install/start", "/storage/dist");
    return handler(request, response);
  }
});

server.listen(80, () => {
  console.log("Running at http://localhost:80");
});
