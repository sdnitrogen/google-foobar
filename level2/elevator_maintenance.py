def solution(l):
    # Your code here
    versions = [ver.split('.') for ver in l]
    intversions = [map(int, ver) for ver in versions]
    intversions.sort()
    return [('.'.join(str(v) for v in ver)) for ver in intversions]
