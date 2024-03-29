import type { IncomingMessage, ServerResponse } from "node:http"
import { createServer } from "node:http"
import { SERVER_BASE_URL } from "@/consts"

const [HOST, PORT] = SERVER_BASE_URL.split("//")[1].split(":")

function getRequestBody(req: IncomingMessage) {
  return new Promise((resolve, reject) => {
    let body = ""
    req.on("data", (chunk) => (body += chunk.toString()))
    req.on("end", () => resolve(JSON.parse(body ?? "{}")))
    req.on("error", reject)
  })
}

async function requestListener(req: IncomingMessage, res: ServerResponse) {
  const body = await getRequestBody(req)
  res.writeHead(200, { "Content-Type": "application/json" })
  res.end(JSON.stringify({ success: true, message: `Data ${body} sent successfully` }))
}

const server = createServer(requestListener)
server.listen(Number(PORT), HOST, () => {
  console.log(`MockServer running on http://${HOST}:${PORT}`)
})
