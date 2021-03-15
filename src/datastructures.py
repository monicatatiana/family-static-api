
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask import Flask, request, jsonify, url_for
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
           { "id" : self._generateId(),
            "first_name" : "John",
            "last_name" : "Jackson",
            "age" : 33,
            "Lucky Numbers" : [7, 13, 22]},
           { "id" : self._generateId(),
            "first_name" : "Jane",
            "last_name" : "Jackson",
            "age" : 35,
            "Lucky Numbers" : [10, 14, 3]},
           { "id" : self._generateId(),
            "first_name" : "Jimmy",
            "last_name" : "Jackson",
            "age" : 5,
            "lucky Numbers" : [1]}

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        
        return None
        

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
            else:
                raise Exception("Member not found")
            return None

    def get_member(self, id):
        # fill this method and update the return
        for i in self._members:
            if i["id"] == int(id):
                return i
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
