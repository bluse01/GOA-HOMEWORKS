
def Grade_Test(gl):
    for name, score in gl.items():
        if score > 59:
            print(f"{name} Pass!")
        else:
            print(f"{name} Fail!")

Grade_Test(
    {
        "James": 60,
        "Mike": 76,
        "Lee": 45
    }
)