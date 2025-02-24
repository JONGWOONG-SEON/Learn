import java.net.Socket
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter

const val HOST = "127.0.0.1"
const val PORT = 4440

fun main() {
    val socket = Socket(HOST, PORT)
    println("[Sidecar] Connected to Main Server at $HOST:$PORT")

    val input = BufferedReader(InputStreamReader(socket.getInputStream()))
    val output = PrintWriter(socket.getOutputStream(), true)

    while (true) {
        val received = input.readLine() ?: break  // 데이터 수신
        println("[Sidecar] Received: $received")

        val response = "Processed $received"
        output.println(response)  // 응답 전송
    }

    socket.close()
}