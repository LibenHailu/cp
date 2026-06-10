import sys

def main():
    # Read all inputs from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Iterator to mimic sequential 'cin >>' behavior
    iterator = iter(input_data)
    
    try:
        t = int(next(iterator))
        
        for _ in range(t):
            n = int(next(iterator))
            
            output_parts = []
            
            # Loop 1: for (int i = 1; i <= n; ++i)
            for i in range(1, n + 1):
                output_parts.append(f"{i} ")
                
            # Loop 2: for (int i = 1; i <= n; ++i)
            for i in range(1, n + 1):
                output_parts.append(f"{i} ")
                
            # Middle print: cout << n << " ";
            output_parts.append(f"{n} ")
            
            # Loop 3: for (int i = 1; i < n; ++i)
            for i in range(1, n):
                output_parts.append(f"{i} ")
                
            # Loop 4: cout << i << (i == n ? "" : " ");
            for i in range(1, n + 1):
                space = "" if i == n else " "
                output_parts.append(f"{i}{space}")
                
            # Print everything for the current test case followed by a newline
            print("".join(output_parts))
            
    except StopIteration:
        pass

if __name__ == '__main__':
    main()