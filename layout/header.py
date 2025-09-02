from nicegui import ui



def header(current_path: str):

    # Drawer (hidden by default, slides from right)
    with ui.drawer(side='right', value=False).props('overlay bordered') as menu_drawer:
        menu_drawer.classes('bg-[#1b3652] text-white w-60 p-4 flex flex-col space-y-2')

        # Drawer header with title + close button
        with ui.row().classes('justify-between items-center mb-4 w-full'):
            ui.label('Navigation').classes('text-lg font-bold')
            ui.button(icon='close', on_click=menu_drawer.toggle).props('flat round dense color=white')

        # Navigation buttons (navigate + close drawer)
        def navigate_and_close(path: str):
            ui.navigate.to(path)
            menu_drawer.toggle()

        ui.button('Home', on_click=lambda: navigate_and_close('/')).props('flat').classes('w-full justify-start text-white')
        ui.button('MQL Automation', on_click=lambda: navigate_and_close('/mql_automation')).props('flat').classes('w-full justify-start text-white')
        ui.button('Opportunity Generator', on_click=lambda: navigate_and_close('/opportunity_generator')).props('flat').classes('w-full justify-start text-white')
        ui.button('PDF to Table', on_click=lambda: navigate_and_close('/pdf_to_table')).props('flat').classes('w-full justify-start text-white')
        ui.button('Ultimate Parent Generator', on_click=lambda: navigate_and_close('/ultimate_parent_generator')).props('flat').classes('w-full justify-start text-white')

    
    with ui.header().style('height: 65px;').classes('bg-[#4281c8] text-black'):

        with ui.row().classes('items-center justify-between w-full px-6'):
            ui.button('WK One Stop Center') \
                .props('rounded') \
                .style('color: white;') \
                .classes('font-yellowtail normal-case bg-black')

            def nav_button(label: str, path: str):
                is_active = current_path == path
                style_class = 'button-bottom-border text-black' if is_active else 'text-white'
                props = 'outline rounded' if is_active else 'flat rounded'

                ui.button(label,
                          on_click=None if is_active else lambda p=path: ui.navigate.to(p)
                          ).props(props).classes(f'font-poppins font-medium normal-case {style_class}')

            with ui.row().classes('gap-4 flex-wrap gt-md'):
                nav_button('Home', '/')
                nav_button('MQL Automation', '/mql_automation')
                nav_button('Opportunity Generator', '/opportunity_generator')
                nav_button('PDF to Table', '/pdf_to_table')
                nav_button('Ultimate Parent Generator', '/ultimate_parent_generator')

            
            # Hamburger
            ui.button(icon='menu', on_click=menu_drawer.toggle).props('flat color=white').classes('lt-lg')
