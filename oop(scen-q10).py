class NetworkUtility:

    @staticmethod
    def is_latency_safe(latency):
        if latency <= 50:
            return True
        return False

print(NetworkUtility.is_latency_safe(45))