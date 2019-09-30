#include <iostream>
#include <string>
#include "speechmanager.h"

using namespace std;

void testSpeaker(){
    SpeechManager sm;
    for(map<int,Speaker>::iterator it=sm.m_Speaker.begin();it!=sm.m_Speaker.end();it++){
        cout  << "选手编号：" << it->first
              << " 姓名： " << it->second.m_name
              << " 成绩： " << it->second.m_score[0] << endl;
    }
}

void chooseButton(){
    SpeechManager sm;
    int choice=0;

    testSpeaker();

    while(true){
        sm.showMenu();
        cout << "请输入您的选择： " << endl;
        cin>>choice;

        switch(choice){
            case 1:  //开始比赛
                sm.startSpeech();
                break;
            case 2:  //查看记录
                sm.showRecord();
                break;
            case 3:  //清空记录
                sm.clearRecord();
                break;
            case 0:  //退出系统
                sm.systemExit();
                break;
            default:
                system("cls"); //清屏
                break;
        }
    }
}


int main() {
    srand((unsigned int)time(NULL));
    chooseButton();
    return 0;

}