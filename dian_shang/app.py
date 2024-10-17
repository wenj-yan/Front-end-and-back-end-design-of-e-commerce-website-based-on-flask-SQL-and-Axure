from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/phone')
def phone():
    return render_template('goods_list/phone.html')


@app.route('/pad')
def pad():
    return render_template('goods_list/pad.html')


@app.route('/tv')
def tv():
    return render_template('goods_list/tv.html')


@app.route('/computer')
def computer():
    return render_template('goods_list/computer.html')


# Phone的商品页面
@app.route('/Xiaomi_MIX_Alpha_slider')
def Xiaomi_MIX_Alpha_slider():
    return render_template('goods_info/phone/Xiaomi_MIX_Alpha_slider.html')


@app.route('/Xiaomi_MIX_Fold_3')
def Xiaomi_MIX_Fold_3():
    return render_template('goods_info/phone/Xiaomi_MIX_Fold_3.html')


@app.route('/Xiaomi_MIX_Fold_2')
def Xiaomi_MIX_Fold_2():
    return render_template('goods_info/phone/Xiaomi_MIX_Fold_2.html')


@app.route('/Xiaomi_14')
def Xiaomi_14():
    return render_template('goods_info/phone/Xiaomi_14.html')


# tv的商品页面
@app.route('/Xiao_mi_A65')
def Xiao_mi_A65():
    return render_template('goods_info/tv/Xiao_mi_A65.html')


@app.route('/Xiao_mi_Master')
def Xiao_mi_Master():
    return render_template('goods_info/tv/Xiao_mi_Master.html')


@app.route('/Xiao_mi_S_65')
def Xiao_mi_S_65():
    return render_template('goods_info/tv/Xiao_mi_S_65.html')


@app.route('/Xiao_mi_S_75')
def Xiao_mi_S_75():
    return render_template('goods_info/tv/Xiao_mi_S_75.html')


# computer页面
@app.route('/Redmi_Book_16_2024')
def Redmi_Book_16_2024():
    return render_template('goods_info/computer/Redmi_Book_16_2024.html')


@app.route('/Redmi_Book_Pro_14_2024')
def Redmi_Book_Pro_14_2024():
    return render_template('goods_info/computer/Redmi_Book_Pro_14_2024.html')


@app.route('/Redmi_Book_Pro_16_2024')
def Redmi_Book_Pro_16_2024():
    return render_template('goods_info/computer/Redmi_Book_Pro_16_2024.html')


@app.route('/Redmi_G_Pro_Game_2024')
def Redmi_G_Pro_Game_2024():
    return render_template('goods_info/computer/Redmi_G_Pro_Game_2024.html')


# Pad商品信息
@app.route('/Redmi_Pad_SE')
def Redmi_Pad_SE():
    return render_template('goods_info/pad/Redmi_Pad_SE.html')


@app.route('/Xiaomi_Pad_6_Max_14')
def Xiaomi_Pad_6_Max_14():
    return render_template('goods_info/pad/Xiaomi_Pad_6_Max_14.html')


@app.route('/Xiaomi_Pad_6_Pro')
def Xiaomi_Pad_6_Pro():
    return render_template('goods_info/pad/Xiaomi_Pad_6_Pro.html')


@app.route('/Xiaomi_Pad_6S_Pro_12')
def Xiaomi_Pad_6S_Pro_12():
    return render_template('goods_info/pad/Xiaomi_Pad_6S_Pro_12.html')

@app.route('/ling_quan')
def ling_quan():
    return render_template('lingquan.html')

@app.route('/manage')
def manage():
    return render_template('manages.html')

@app.route('/shangpin')
def shangpin():
    return render_template('shangpin.html')

@app.route('/fabu')
def fabu():
    return render_template('houtai/系统首页.html')

if __name__ == '__main__':
    app.run(debug=True)
#192.168.9.209