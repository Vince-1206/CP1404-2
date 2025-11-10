BoxLayout:
    orientation: 'vertical'

    BoxLayout:          # Row 1
        Button:
            text: 'Genesis'

    BoxLayout:          # Row 2 (vertical group)
        orientation: 'vertical'
        Button:
            text: 'Exodus'
        Button:
            text: 'Leviticus'
        Button:
            text: 'Numbers'

    BoxLayout:          # Row 3 (small height)
        size_hint_y: 0.1
        Button:
            text: 'Deuteronomy'
