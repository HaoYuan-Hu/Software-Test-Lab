private String find(String key, Deque<LogFile> logFileDeque) {

    final List<LogFile> collect =
            logFileDeque.stream().filter(x -> idx.idxOf(x, key) != -1).collect(Collectors.toList());

    if (collect.size() > 0) {
        LogFile logFile = collect.get(collect.size() - 1);  // 寻找最新的那一个
        return Util.valueOf(logFile.read(idx.idxOf(logFile, key)));
    } else {
        return "";
    }
}