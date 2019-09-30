//
// Created by 李涛 on 9/26/19.
//

#ifndef SPEECHMATCH_SPEECHMANAGER_H
#define SPEECHMATCH_SPEECHMANAGER_H

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "speaker.h"

using namespace std;

class SpeechManager{
public:
    //构造函数
    SpeechManager();

    //菜单展示功能
    void showMenu();

    //退出功能
    void systemExit();

    //比赛选手 容器  12人,存放的是选手编号
    vector<int>v1;

    //第一轮晋级容器  6人，存放的是选手编号
    vector<int>v2;

    //胜利前三名容器  3人，存放的是选手编号
    vector<int>vVictory;

    //存放编号 以及对应的 具体选手 容器
    map<int, Speaker> m_Speaker;

    //初始化属性
    void initSpeech();

    //比赛轮次
    int m_index=0;

    //创建选手
    void createSpeaker();

    //开始比赛
    void startSpeech();

    // 抽签
    void speechDraw();

    // start a contest
    void speechContext();

    // show score
    void showScore();

    // save record
    void saveRecord();

    // read record
    //往届记录
    map<int, vector<string>> m_Record;
    bool fileIsEmpty=false;
    void readRecord();

    void showRecord();

    //clear record
    void clearRecord();

    // 析构函数
    ~SpeechManager();


};

#endif //SPEECHMATCH_SPEECHMANAGER_H
