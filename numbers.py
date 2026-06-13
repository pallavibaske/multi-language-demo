def lambda_handler(event, context):

    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    highest = max(numbers)
    lowest = min(numbers)
    average = sum(numbers) / len(numbers)

    return {
        "statusCode": 200,
        "body": {
            "numbers": numbers,
            "highest": highest,
            "lowest": lowest,
            "average": average
        }
    }
