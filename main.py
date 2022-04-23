# -*- coding: utf-8 -*-
"""
@function： 使用GUI模块和处理模块构造主函数以实现计算并显示三角函数\n
@author: 敖钰民\n
@time： 2022年4月23日14:58:11
"""

import GUI
from function_Final import *
import sys
from input_detect import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial


# 处理GUI的事件的函数
def calculator(ui):
    """
        当用户按下计算时，在这里处理
        :param ui:pyqt5创建的ui类的对象
        :return:
                0：正常退出
                -1：不能转为float
                -2：模式设置错误
                -3：函数设置错误
                -4：输入范围不对
        """
    # 输入框内容
    input0 = ui.input.text()
    # 选择的函数（sin,cos等）
    fnc = ui.fnc
    # 选择的模式（角度/弧度）
    md = ui.md

    # 判断是否为float
    if not isFloat(input0):
        ui.output.setText("类型错误，请重输")
        return -1
    # 判断是否超出处理范围
    else:
        input0 = float(input0)
        if abs(input0) > 999999999:
            ui.output.setText("输入值过大")
            return -4
        # 判断弧度制还是角度制
        if md == "角度制":
            input0 = (input0 * 3.141592653589793) / 180
        elif (md != "角度制") and (md != "弧度制"):
            ui.output.setText("模式设置错误")
            print("GUI错误：模式库里面没有{}模式".format(md))
            return -2
        # 根据选择的函数类型进行计算
        if fnc == "sin":
            result = mySin(input0)
        elif fnc == "cos":
            result = myCos(input0)
        elif fnc == "arcsin":
            # 检查是否超出arcsin定义域
            if (input0 > 1) or (input0 > 1):
                ui.output.setText("输入绝对值不应大于1")
                return -4
            result = asin(input0)
        elif fnc == "arctan":
            result =atan(input0)
        else:
            ui.output.setText("函数设置错误")
            print("GUI错误：函数库里面没有{}函数".format(fnc))
            return -3
    print("calculate: func:{}, mode:{}, value:{}, result:{}".format(fnc, md, input0, result))
    # 输出框显示
    ui.output.setText(str(result))
    return 0

if __name__ == '__main__':
    # 创建程序
    app = QApplication(sys.argv)
    # 定义主窗口
    MainWindow = QMainWindow()
    # 定义UI
    ui = GUI.Ui_HelloWorld()
    # 设置UI
    ui.setupUi(MainWindow)
    # 显示窗口
    MainWindow.show()

    # 开始进入到数据处理
    ui.cal_Button.clicked.connect(partial(calculator, ui))  # 如果按钮被点击，则调用convert函数

    sys.exit(app.exec_())