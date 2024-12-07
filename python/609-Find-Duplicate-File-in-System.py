from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        data: dict[str, list[str]] = defaultdict(list)
        for path in paths:
            directory, files = path.split(' ', 1)
            for file in files.split():
                file_content = file[file.index('('):-1]
                data[file_content].append(directory+'/'+file[0:file.index('(')])
        
        return [v for _, v in data.items() if len(v) >= 2]

#T: O(N*M) N = len(paths), M = len(files)
#S: O(N*M)
