#!/usr/bin/python3
def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
    return prime_numbers

def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    max_num = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_num)
    prime_set = set(prime_numbers)
    
    def game_result(n):
        remaining = set(range(1, n + 1))
        current_player = 0  # Maria starts, 0 for Maria, 1 for Ben
        
        while prime_set.intersection(remaining):
            for p in prime_numbers:
                if p in remaining:
                    multiples = set(range(p, n + 1, p))
                    remaining -= multiples
                    break
            current_player = 1 - current_player  # Switch player
        
        return 1 - current_player  # Return the winner (1 - current_player)

    results = [game_result(n) for n in nums]
    maria_wins = results.count(0)
    ben_wins = results.count(1)

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
