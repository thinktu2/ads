# Paxos 算法测试

## 编译与运行脚本

```shell
bash run.sh
```

全部输出内容在文件 `/root/out.txt` 中

## 修改

编译警告

```shell
src/Paxos.cpp: In function 'void* Proposer(void*)':
src/Paxos.cpp:24:43: warning: format '%d' expects argument of type 'int', but argument 3 has type 'long int' [-Wformat=]
  sprintf( logName, "Proposer%d", (long)id );
                                  ~~~~~~~~ ^
src/Paxos.cpp: In function 'int main(int, char**)':
src/Paxos.cpp:152:54: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
  for ( i = 0; i < 5; i++ ) t[i].Run(Proposer, (void*)i);
                                                      ^
src/lib/Logger.cpp: In member function 'bool mdk::Logger::Info(const char*, const char*, ...)':
src/lib/Logger.cpp:288:75: warning: format '%llu' expects argument of type 'long long unsigned int', but argument 4 has type 'mdk::uint64 {aka long unsigned int}' [-Wformat=]
   fprintf(m_fpRunLog, "%s Tid:%llu [%s] ", strTime, CurThreadId(), findKey);
                                                     ~~~~~~~~~~~~~         ^
src/lib/Logger.cpp:303:63: warning: format '%llu' expects argument of type 'long long unsigned int', but argument 3 has type 'mdk::uint64 {aka long unsigned int}' [-Wformat=]
    printf("%s Tid:%llu [%s] ", strTime, CurThreadId(), findKey);
                                         ~~~~~~~~~~~~~         ^
src/lib/Logger.cpp: In member function 'bool mdk::Logger::StreamInfo(const char*, unsigned char*, int, const char*, ...)':
src/lib/Logger.cpp:332:75: warning: format '%llu' expects argument of type 'long long unsigned int', but argument 4 has type 'mdk::uint64 {aka long unsigned int}' [-Wformat=]
   fprintf(m_fpRunLog, "%s Tid:%llu [%s] ", strTime, CurThreadId(), findKey);
                                                     ~~~~~~~~~~~~~         ^
src/lib/Logger.cpp:341:63: warning: format '%llu' expects argument of type 'long long unsigned int', but argument 3 has type 'mdk::uint64 {aka long unsigned int}' [-Wformat=]
    printf("%s Tid:%llu [%s] ", strTime, CurThreadId(), findKey);
                                         ~~~~~~~~~~~~~         ^
```

1. `src/Paxos.cpp:24:43` 处, 将 `%d` 修改为 `%ld`
2. `src/Paxos.cpp:152:54` 处, 将 `i` 修改为 `long` 类型
3. `src/lib/Logger.cpp` 中的警告, 将 `%llu` 修改为 `%lu`
