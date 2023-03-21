# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None

    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Running...')

        design = app.activeProduct
        rootComp = design.rootComponent
        componentCount = {}

        for occurrence in rootComp.allOccurrences:
            if occurrence.component.name in componentCount:
                componentCount[occurrence.component.name] += 1
            else:
                componentCount[occurrence.component.name] = 1

        table = []

        for name, count in componentCount.items():
            table.append([name, count])

        output_text = '\n'.join([f'{name} -> {count}' for name, count in table])
        output_text += f'\nTotal Unique Components -> {len(table)}'
        output_text += f'\nTotal Components -> {sum([count for name, count in table])}'

        output_lines = output_text.split('\n')
        max_lines = 25

        for i in range(0, len(output_lines), max_lines):
            ui.messageBox('\n'.join(output_lines[i:i+max_lines]))
        

    except:
        if ui:
            ui.messageBox(f'Failed:\n{traceback.format_exc()}')
