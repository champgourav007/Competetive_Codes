def disconnect_notes(notes):
    operations = 0
    start = 0
    end = len(notes) - 1

    while start < end:
        if notes[start] != notes[end]:
            operations += 1
        start += 1
        end -= 1

    return operations

# Example usage
notes = 'abcddcba'
min_operations = disconnect_notes(notes)
print(min_operations)
