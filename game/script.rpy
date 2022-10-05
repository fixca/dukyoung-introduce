# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.


# 여기에서부터 게임이 시작합니다.

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("경영회계과"))

    Tutorial("introducing_management_first", "경영회계과 1학년은 무엇을 하나요?")

    # Tutorial("introducing_makerspace", _("메이커 스페이스가 어떤 곳인가요?"))
    # Tutorial("introducing_restaurant", _("교내 식당은 어떻게 생겼나요?"))
    # Tutorial("introducing_classroom_software", _("소프트웨어과의 교실은 어떻게 생겼나요?"))
    # Tutorial("introducing_bookcafe", _("북카페는 어떻게 생겼나요?"))

    Section(_("보건간호과"))

    Tutorial("introducing_health_first", "보건간호과 1학년은 무엇을 하나요?")
    Tutorial("introducing_health_company", "보건간호과는 취업을 어디로 할 수 있나요?")

    Section(_("빅데이터과"))

    Tutorial("introducing_dickdata_first", "빅데이터과 1학년은 무엇을 하나요?")
    Tutorial("introducing_dickdata_company", "빅데이터과는 취업을 어디로 할 수 있나요?")

    Section(_("소프트웨어과 (인공지능)"))

    Tutorial("introducing_soft_ai_first", "소프트웨어 (인공지능)과 1학년은 무엇을 하나요?")

    Section(_("소프트웨어과 (정보보안)"))

    Tutorial("introducing_soft_secure_first", "소프트웨어 (정보보안)과 1학년은 무엇을 하나요?")
    

screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _(""):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True

image testBackGround:
    im.FactorScale("images/background/test_background.png", 0.31746031746031746031746031746032)
    yalign 0.0
    xalign 0.0
    # "images/background/test_background.png"
    

label start:

    scene testBackGround with fade

    "덕영 고등학교에 오신것을 환영합니다!"

    "이 곳에서는, 덕영 고등학교의 다양한 시설과 환경을 간단한 게임으로 체험해볼 수 있습니다!"

    jump callScrollBar

    

label callScrollBar:

    

    if tutorials_first_time:
        "그럼 원하시는 항목을 화면에서 선택해주세요!"
    else :
        scene testBackGround with fade
        "다른 궁금한점이 있으신가요?"
    
    $ tutorials_first_time = False
    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    $ reset_example()

    call expression tutorial.label from _call_expression
    
    jump callScrollBar

label end:

    "이용해주셔서 감사합니다!"

    return
