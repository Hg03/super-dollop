import flet as ft


def main(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True
    degree_p = ft.TextField(label="Degree (%)", autofocus=True)
    degree_t = ft.TextField(label="Degree (in Subject)")
    gender = ft.TextField(label='Gender')
    ssc_p = ft.TextField(label='SSC (%)')
    ssc_b = ft.TextField(label = 'SSC (branch)')
    hsc_p = ft.TextField(label = 'HSC (%)')
    hsc_b = ft.TextField(label = 'HSC (branch)')
    hsc_s = ft.TextField(label = 'HSC (subject)')
    workex = ft.TextField(label = 'Work Experience')
    etest_p = ft.TextField(label = 'Etest (%)')
    specialisation = ft.TextField(label = 'Specialisation')
    mba_p = ft.TextField(label = 'MBA (%)')
    salary = ft.TextField(label = 'Salary')
    content=ft.Text(value='Campus Recruitment Prediction',text_align=ft.TextAlign.CENTER,color='green',weight=ft.FontWeight.BOLD)
    predictions = ft.Column()

    def btn_click(e):
        predictions.controls.append(ft.Text(f"{degree_p.value}"))
        degree_p.value = ""
        degree_t.value = ""
        gender.value = ""
        ssc_p.value = ""
        ssc_b.value = ""
        hsc_p.value = ""
        hsc_b.value = ""
        hsc_s.value = ""
        workex.value = ""
        etest_p.value = ""
        specialisation.value = ""
        mba_p.value = ""
        salary.value = ""
        page.update()
        degree_p.focus()

    page.add(
            #ft.Row([content]),
            content,
            ft.ResponsiveRow([ft.Column(col=6,controls=[degree_p]),ft.Column(col=6,controls = [degree_t])]),
            gender,
            ft.ResponsiveRow([ft.Column(col=6,controls=[ssc_p]),ft.Column(col=6,controls = [ssc_b])]),
            ft.ResponsiveRow([ft.Column(col=4,controls=[hsc_p]),ft.Column(col=4,controls = [hsc_b]),ft.Column(col=4,controls = [hsc_s])]),
            workex,
            etest_p,
            specialisation,
            mba_p,
            salary,
            ft.ElevatedButton('Predict the Recruitment Rate',on_click=btn_click,col=6),
            predictions
    )
        
    

ft.app(target=main,view=ft.WEB_BROWSER)