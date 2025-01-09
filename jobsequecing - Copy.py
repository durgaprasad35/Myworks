class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline to determine the number of slots needed
    max_deadline = max(job.deadline for job in jobs)

    # Initialize result and slot tracker
    result = [-1] * max_deadline  # Tracks job IDs in their slots
    occupied = [False] * max_deadline  # Tracks if a slot is occupied

    # Schedule jobs to maximize profit
    for job in jobs:
        # Try to fit the job into a slot before its deadline
        for slot in range(min(job.deadline - 1, max_deadline - 1), -1, -1):
            if not occupied[slot]:
                occupied[slot] = True
                result[slot] = job.job_id
                break

    # Filter out empty slots and return the sequence
    return [job_id for job_id in result if job_id != -1]

# Example usage
if __name__ == "__main__":
    jobs = [
        Job("Job1", 2, 100),
        Job("Job2", 1, 50),
        Job("Job3", 2, 10),
        Job("Job4", 1, 20),
        Job("Job5", 3, 30)
    ]

    optimal_sequence = job_sequencing(jobs)
    print("Optimal Job Sequence:", optimal_sequence)
