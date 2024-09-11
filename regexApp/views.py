from typing import Any
from django.shortcuts import render, redirect
from regexApp.urls import *
from regexApp.models import *
from . import forms
import re
import subprocess as sp

# Create your views here.
def index(request: Any) -> Any:
    form=forms.regexPatternForm(data=request.POST)
    return render(request=request, template_name='index.html', context={'form': form})

def uploadFile(request: Any) -> Any | None:
    if request.method=="POST":
        form=forms.regexPatternForm(data=request.POST, files=request.FILES or None,)
        if form.is_valid():
            form.save()
            return redirect(to='logicForRegexPattern', context={'form': form},)
    else:
        form=forms.regexPatternForm()
    return render(request=request, template_name='upload.html', context={'form': form},)
    
def logicForRegexPattern(request)-> None:
    # Define patterns
    grabContent = re.compile(pattern=r'\[(.+?)\](.*?)(?=\n\[|$)', flags=re.DOTALL,) 
    grabLinesOtherThan = re.compile(pattern=r'^(?!;)(.+)', flags=re.MULTILINE,)

    # Read the content from the file
    with open(file=f'{request.FILES['file']}', mode="r",) as infile:
        content = infile.read()

    # Find matches in the content
    matches = grabContent.findall(string=content,)
    patternsDict = {title.strip(): content.strip() for title, content in matches}

    # Process each pattern
    for key, value in patternsDict.items():
        matchesForExtractingData = grabLinesOtherThan.findall(string=value,)
        
        # Format the data
        formatted_lines = []
        for line in matchesForExtractingData:
            items = re.split(pattern=r'\s+', string=line.strip(),)
            formatted_items = []
            for item in items:
                if item == ';':
                    formatted_items.append('null;')
                else:
                    formatted_items.append(item)
                    
            formatted_line = ', '.join(formatted_items)
            formatted_lines.append(formatted_line)
        
        # Print formatted data for each key
        if key == "JUNCTIONS":
            outputKey=sp.check_output(args=key, shell=True)
            for formatted_line in formatted_lines:
                outputValue=sp.check_output(args=formatted_line, shell=True)
            return render(request="request", template_name='index.html', context={'outputKey': outputKey, 'outputValue': outputValue})