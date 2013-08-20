#!/usr/bin/python
# -*- coding: utf-8 -*-
from project import Project
from document import Document
from clause import Clause

path = './Exemplo/Larissa.prj'

project = Project()
project.loadXML(path)
