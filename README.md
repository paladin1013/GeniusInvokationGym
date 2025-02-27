<!--
 Copyright (c) 2022 davidgao

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->


非常抱歉，由于作者近期时间有限，本项目暂停开发。

请关注[谷雨同学](https://guyutongxue.site/)已完成开发且持续更新的[七圣召唤模拟器](https://github.com/Guyutongxue/genius-invokation)，欢迎[试玩](https://gi-tcg.vercel.app/)

# Genius Invokation Gym

A simple simulator of the Genius Invokation TCG in Genshin impact

API will be designed based on [rlcard](https://github.com/datamllab/rlcard)

Simulator framework references [fireplace](https://github.com/jleclanche/fireplace)

Package name `gisim` stands for both `Genshin Impact` and `Genius Invokation`

一个简易的七圣召唤仿真器（如果不弃坑的话）

希望可以实现类似openai-gym的API，用于训练ai&评估卡组强度

简单介绍请参考[该Notion页面](https://paladin1013.notion.site/gisim-A-Genius-Invokation-Simulator-4743c9996d094e3088ea91f47e70711b?pvs=4)


# Get Started

Prerequisites:
* Python >=3.8
* [Poetry 1.1.14+](https://python-poetry.org)

Installation: enter the project directory and execute the following command:
```bash
poetry install
```
(Optional) You can also try to install this package with pip:
```bash
pip3 install .
```

Runnable basic demo locally: give the following a try:
```bash
poetry run python3 -u tests/test_framework.py
```


# Roadmap
- [x] Encode the game status into a dictionary
- [x] Define all kinds of messages for communication
- [x] Use message queue (with priority) to buffer all messages
- [ ] Enable judging validity of a proposed action
- [ ] Add message handler to every character, summon, status, ...
    - [x] Finish normal attack, elemental skill, elemental burst of KamisatoAyaka (as a template to generate more characters in the future)
    - [x] Add Summon and Elemental Infusion based on KamisatoAyaka
- [ ] Currently available roles
    - [x] Kamisato Ayaka
    - [x] Maguu Kenki
    - [x] Sucrose


新建QQ交流群613071650，欢迎感兴趣的同学入群，欢迎成为Contributor！


## Works Cited

[RLCard: A Toolkit for Reinforcement Learning in Card Games](https://github.com/datamllab/rlcard)

[DouZero: Mastering DouDizhu with Self-Play Deep Reinforcement Learning](https://github.com/kwai/DouZero)
