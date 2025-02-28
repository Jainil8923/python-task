from typing import List, Dict

def atd(arr: List[str]) -> Dict[int,str]:
    return {i: arr[i] for i in range(len(arr))}