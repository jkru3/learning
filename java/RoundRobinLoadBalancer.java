import java.util.Arrays;

public class RoundRobinLoadBalancer {
    public static void main(String[] args) {
        // Example inputs
        int n = 4; // Number of servers
        int[] arrival = {3, 5, 1, 6, 8}; // Arrival times of requests
        int[] burstTime = {9, 2, 10, 4, 5}; // Burst times of each request

        int[] serverAssignments = assignRequestsToServers(n, arrival, burstTime);
        System.out.println("Server assignments: " + Arrays.toString(serverAssignments));
    }

    public static int[] assignRequestsToServers(int n, int[] arrival, int[] burstTime) {
        int[] serverAvailability = new int[n];
        int[] serverAssignment = new int[arrival.length];

        // Processing each request
        for (int i = 0; i < arrival.length; i++) {
            serverAssignment[i] = -1; // Initially marking as dropped
            for (int j = 0; j < n; j++) {
                // Check if the server is available
                if (serverAvailability[j] <= arrival[i]) {
                    // Assign server
                    serverAssignment[i] = j + 1; // +1 to index from 1 to n
                    // Update server availability time
                    serverAvailability[j] = arrival[i] + burstTime[i];
                    break;
                }
            }
        }

        return serverAssignment;
    }
}