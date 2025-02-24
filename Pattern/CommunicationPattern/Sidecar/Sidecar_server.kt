import java.net.ServerSocket
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter

const val PORT = 4440

fun main() {
    val serverSocket = ServerSocket(PORT)
    println("[Main] Server listening on port $PORT...")

    val clientSocket = serverSocket.accept()
    println("[Main] Connected to Sidecar: ${clientSocket.inetAddress.hostAddress}")

    val input = BufferedReader(InputStreamReader(clientSocket.getInputStream()))
    val output = PrintWriter(clientSocket.getOutputStream(), true)

    repeat(5) { i ->
        val message = "Task ${i + 1} from Main"
        println("[Main] Sending: $message")
        output.println(message)

        val response = input.readLine()
        println("[Main] Received from Sidecar: $response")

        Thread.sleep(1000)
    }

    clientSocket.close()
    serverSocket.close()
}