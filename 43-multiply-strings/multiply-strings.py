class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)

        # Maximum possible length is n1 + n2
        result = [0] * (n1 + n2)

        # Multiply each digit
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                # Positions where the product contributes
                pos1 = i + j
                pos2 = i + j + 1

                result[pos2] += product

                # Handle carry
                result[pos1] += result[pos2] // 10
                result[pos2] %= 10

        # Remove leading zeros
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))