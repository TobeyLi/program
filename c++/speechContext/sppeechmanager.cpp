//
// Created by 李涛 on 9/26/19.
//
#include <iostream>
#include "speechmanager.h"
#include <string>
#include <map>
#include <deque>
#include <functional>
#include <numeric>
#include <fstream>



using namespace std;

SpeechManager::SpeechManager(){
    // 开始比赛之前需要初始化所有的内容
    this->initSpeech();

    // 创建选手
    this->createSpeaker();

    // read the record
    this->readRecord();

    // 初始化记录容器
    this->m_Record.clear();
}

SpeechManager::~SpeechManager()
{
}

void SpeechManager::showMenu() {
    cout << "********************************************" << endl;
    cout << "*************  欢迎参加演讲比赛 ************" << endl;
    cout << "*************  1.开始演讲比赛  *************" << endl;
    cout << "*************  2.查看往届记录  *************" << endl;
    cout << "*************  3.清空比赛记录  *************" << endl;
    cout << "*************  0.退出比赛程序  *************" << endl;
    cout << "********************************************" << endl;
    cout << endl;
}

void SpeechManager::systemExit() {
    exit(0);
}


void SpeechManager::initSpeech() {
    // 初始化之前将所有的容器清空
    this->v1.clear();
    this->v2.clear();
    this->vVictory.clear();
    this->m_Speaker.clear();

    this->m_index=1;
}

void SpeechManager::createSpeaker() {
    string nameSeed="ABCDEFGHIJKL";
    for(int i=0;i<nameSeed.size();i++){
        // 初始化姓名
        string name = "选手";
        name += nameSeed[i];

        Speaker sp;
        sp.m_name=name;

        // 初始化得分
        for(int j=0;j<2;j++){
            sp.m_score[j]=0;
        }

        //12名选手编号
        this->v1.push_back(i + 10001);

        //选手编号 以及对应的选手 存放到map容器中
        this->m_Speaker.insert(make_pair(i + 10001, sp));

    }
}

// 比赛流程实现
void SpeechManager::startSpeech() {
    //第一轮比赛
    //1、抽签
    this->speechDraw();
    //2、比赛
    this->speechContext();
    //3、显示晋级结果
    this->showScore();

    //第二轮比赛
    this->m_index++;
    //1、抽签
    this->speechDraw();

    //2、比赛
    this->speechContext();

    //3、显示最终结果
    this->showScore();

    //4、保存分数
    this->saveRecord();

    //解决没有实时更新的问题
    this->initSpeech();
    this->createSpeaker();
    this->readRecord();
}

// 抽签函数实现
void SpeechManager::speechDraw(){
    // 只是需要将选手的序号打乱即可
    cout << "第 << " << this->m_index << " >> 轮比赛选手正在抽签"<<endl;
    cout << "---------------------" << endl;
    cout << "抽签后演讲顺序如下：" << endl;
    if (this->m_index == 1){
        random_shuffle(v1.begin(), v1.end());
        for (vector<int>::iterator it = v1.begin(); it != v1.end(); it++){
            cout << *it << " ";
        }
        cout << endl;
    }
    else{
        random_shuffle(v2.begin(), v2.end());
        for (vector<int>::iterator it = v2.begin(); it != v2.end(); it++){
            cout << *it << " ";
        }
        cout << endl;
    }
    cout << "---------------------" << endl;
    cout << endl;
}

// 开始比赛
void SpeechManager::speechContext() {

    multimap<double ,int,greater<int>> groupScore; //临时容器，保存key分数 value 选手编号
    vector <int>v_Src;   //比赛的人员容器
    if (this->m_index == 1){
        v_Src = v1;
    }
    else{
        v_Src = v2;
    }
    int num = 0; //记录人员数，6个为1组

    // 直接给每个人员进行打分
    for(vector<int>::iterator it=v_Src.begin();it!=v_Src.end();it++){
        num++;
        //十个评委，分别打分
        deque<double> d;

        for(int i=0;i<10;i++){
            double score=0;
            score=(rand() % 401 + 600) / 10.f;  // 600 ~ 1000
            d.push_back(score);
        }

        //排序
        sort(d.begin(),d.end(),greater<double>());

        //去掉一个最高分以及一个最低分
        d.pop_front();
        d.pop_back();

        // 计算总和
        double sum=accumulate(d.begin(),d.end(),0.0f);

        // 计算均分
        double avg = sum / (double)d.size();

        this->m_Speaker[*it].m_score[this->m_index - 1]=avg;


        //6个人一组，用临时容器保存
        groupScore.insert(make_pair(avg, *it));
        if (num % 6 == 0){

            cout << "第" << num / 6 << "小组比赛名次：" << endl;
            for (multimap<double, int, greater<int>>::iterator it = groupScore.begin(); it != groupScore.end(); it++)
            {
                cout << "编号: " << it->second << " 姓名： " << this->m_Speaker[it->second].m_name << " 成绩： " << this->m_Speaker[it->second].m_score[this->m_index - 1] << endl;
            }

            int count = 0;
            //取前三名
            for (multimap<double, int, greater<int>>::iterator it = groupScore.begin(); it != groupScore.end() && count < 3; it++, count++){
                if (this->m_index == 1){
                    v2.push_back((*it).second);
                }
                else{
                    vVictory.push_back((*it).second);
                }
            }

            groupScore.clear();

            cout << endl;

        }
    }
    cout << "------------- 第" << this->m_index << "轮比赛完毕  ------------- " << endl;

}

void SpeechManager::showScore(){
    cout << "---------第" << this->m_index << "轮晋级选手信息如下：-----------" << endl;
    vector<int>v;
    if (this->m_index == 1){
        v = v2;
    }
    else{
        v = vVictory;
    }

    for (vector<int>::iterator it = v.begin(); it != v.end(); it++){
        cout << "选手编号：" << *it << " 姓名： " << m_Speaker[*it].m_name << " 得分： " << m_Speaker[*it].m_score[this->m_index - 1] << endl;
    }
    cout << endl;
}


void SpeechManager::saveRecord() {
    fstream ofs;

    // 用输出的方式打开文件  -- 写文件
    ofs.open("../speech.csv", ios::out | ios::app);

    //将每个人数据写入到文件中
    for (vector<int>::iterator it = vVictory.begin(); it != vVictory.end(); it++){
        ofs << *it << ","
            << m_Speaker[*it].m_score[1] << ",";
    }
    ofs << endl;

    //关闭文件
    ofs.close();

    cout << "记录已经保存" << endl;
    this->fileIsEmpty= false;
}

void SpeechManager::readRecord() {
    ifstream ifs;
    ifs.open("../speech.csv",ios::in);

    if (!ifs.is_open()){
        this->fileIsEmpty = true;
        cout << "文件不存在！" << endl;
        ifs.close();
        return;
    }

    // 先尝试读取一个字符，
    char ch;
    ifs>>ch;
    if(ifs.eof()){
        cout << "文件为空!" << endl;
        this->fileIsEmpty = true;
        ifs.close();
        return;
    }

    //文件不为空，将读取的字符放回去
    ifs.putback(ch);

    string data;
    int index=0;

    while(ifs>>data) {
        vector<string> v;

        int pos = -1;
        int start = 0;

        while (true) {
            pos = data.find(",", start); //从0开始查找 ','
            if (pos == -1) {
                break; //找不到break返回
            }
            string tmp = data.substr(start, pos - start); //找到了,进行分割 参数1 起始位置，参数2 截取长度
            v.push_back(tmp);
            start = pos + 1;
        }
        this->m_Record.insert(make_pair(index, v));
        index++;
    }
    ifs.close();
}

void SpeechManager::showRecord(){
    if(this->fileIsEmpty== true){
        cout<<"file doesn't exist"<<endl;
        exit(0);
    }
    for (int i = 0; i < this->m_Record.size(); i++){
        cout << "第" << i + 1 << "届 " <<
             "冠军编号：" << this->m_Record[i][0] << " 得分：" << this->m_Record[i][1] << " "
                                                                                  "亚军编号：" << this->m_Record[i][2] << " 得分：" << this->m_Record[i][3] << " ""季军编号：" << this->m_Record[i][4] << " 得分：" << this->m_Record[i][5] << endl;
    }
}

void SpeechManager::clearRecord(){
    cout << "确认清空？" << endl;
    cout << "1、确认" << endl;
    cout << "2、返回" << endl;

    int select = 0;
    cin >> select;

    if (select == 1){
        //打开模式 ios::trunc 如果存在删除文件并重新创建
        ofstream ofs("../speech.csv", ios::trunc);
        ofs.close();

        //初始化属性
        this->initSpeech();

        //创建选手
        this->createSpeaker();

        //获取往届记录
        this->readRecord();


        cout << "清空成功！" << endl;
    } else{
        cout<<"撤销删除删除..."<<endl;
    }
}