#!/bin/bash
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
