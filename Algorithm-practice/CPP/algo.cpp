// window는 fork()나 wait()가 없어 유닉스 환경에서 실행해야 한다.
// 리눅스 우분투 환경에서 실행하였다.

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    pid_t child_pid;
    int status, i;

    child_pid = fork();

    if(child_pid > 0){
        // 부모 프로세스
        pid_t wait_pid;
        printf("부모 PID: %ld, child pid : %d, errno: %d \n", (long)getpid(), child_pid, errno);

        // 자식 프로세스의 id를 wait_pid에 저장한다.
        // 자식 프로세스가 exit()로 넘겨준 값을 status에 저장한다.
        wait_pid = wait(&status);

        if(wait_pid == -1){
            printf("errno: %d \n", errno);
            perror("wait 함수 오류 반환");
        } else{
            if(WIFEXITED(status)) {
                // 정상 종료 되었을 때, WIFEXITED(status) 매크로가 true를 반환한다.
                // 상위 8비트를 참조하여 자식 프로세스가 exit()에 넘겨준 인자 값을 WEXITSTATUS(status) 매크로를 사용하여 얻을 수 있다.
                printf("wait : 자식 프로세스(%d) 정상 종료, return: %d\n", wait_pid, WEXITSTATUS(status));

                // WEXITSTATUS(status)를 사용하지 않으면 하위 8비트에 0이 채워진 값이 출력된다.
                // 즉, b/100000000 = 256이 출력된다.
                printf("wait : 자식 프로세스(%d) 정상 종료, return: %d\n", wait_pid, status);
            }
            else if(WIFSIGNALED(status)) {
                // 비정상 종료 되었을 때, WIFSIGNALED(status) 매크로가 true를 반환한다.
                // WTERMSIG(status) 매크로를 통해 하위 8에 저장되어 있는 프로세스를 종료시킨 시그널의 번호를 출력한다.
                printf("wait : 자식 프로세스(%d) 정상 종료, return: %d\n", wait_pid, WTERMSIG(status));
                // 하위 8비트에 시그널의 번호가 저장되어 있으므로 같은 결과를 출력한다.
                printf("wait : 자식 프로세스(%d) 정상 종료, return: %d\n", wait_pid, status);
            }
        }

        printf("부모 종료, PID: %ld SIG: %d\n", (long)getpid(), WTERMSIG(status));

    } else if(child_pid == 0){  
        // 자식 프로세스
        printf("자식 PID : %ld \n",(long)getpid());

        sleep(100);
 
        printf("자식 종료\n");
        exit(1);
    }
    else {  
        // fork 실패
        perror("fork Fail! \n");
        return -1;
    }
     
    return 0;
}