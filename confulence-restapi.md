# Confluence REST API examples

## On This Page

- Browse content
- Browse content with pagination
- Read content, and expand the body
Find pages or blogs
Create a new page
Create a new page (jQuery)
Create a new page as a child of another page
Update a page
Delete a page
Upload an attachment
Download an attachment
Get comments from a page
Add a comment to a page (Python)
Create a page with a task
Create a space
Converting content
This page contains examples of using the Confluence Content REST API using curl. The responses are piped into python -mjson.tool (JSON encoder / decoder) to make them easier to read.

Because the REST API is based on open standards, you can use any web development language to access the API.

These examples use basic authentication with a username and password. You can also create a personal access token for authentication (Confluence 7.9 and later).

## Browse content
This example shows how you can browse content. If you're using Confluence 7.18 or later, there's a more performant option that might be useful below.


Copy
curl -u admin:admin http://localhost:8090/rest/api/content?limit=2 | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "393219",
            "type": "page",
            "status": "current",
            "title": "First space",
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/First+space",
                "edit": "/pages/resumedraft.action?draftId=393219",
                "tinyui": "/x/AwAG",
                "self": "http://localhost:8090/rest/api/content/393219"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393219/child",
                "restrictions": "/rest/api/content/393219/restriction/byOperation",
                "history": "/rest/api/content/393219/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393219/descendant",
                "space": "/rest/api/space/FS"
            }
        },
        {
            "id": "393229",
            "type": "page",
            "status": "current",
            "title": "Page 1",
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/Page+1",
                "edit": "/pages/resumedraft.action?draftId=393229&draftShareId=f16d9e64-9373-4719-9df5-aec8102e5252",
                "tinyui": "/x/DQAG",
                "self": "http://localhost:8090/rest/api/content/393229"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393229/child",
                "restrictions": "/rest/api/content/393229/restriction/byOperation",
                "history": "/rest/api/content/393229/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393229/descendant",
                "space": "/rest/api/space/FS"
            }
        }
    ],
    "start": 0,
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/rest/api/content",
        "next": "/rest/api/content?limit=2&start=2",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}
Browse content (Confluence 7.18 and later)
This example shows how you can browse content in Confluence 7.18 and later. The scan endpoint provides better performance, but can only be used to browse pages (not blogs), and doesn't support offset, title, or creationdate parameters.


Copy
curl -u admin:admin http://localhost:8090/rest/api/content/scan?limit=2 | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "393219",
            "type": "page",
            "status": "current",
            "title": "First space",
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/First+space",
                "edit": "/pages/resumedraft.action?draftId=393219",
                "tinyui": "/x/AwAG",
                "self": "http://localhost:8090/rest/api/content/393219"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393219/child",
                "restrictions": "/rest/api/content/393219/restriction/byOperation",
                "history": "/rest/api/content/393219/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393219/descendant",
                "space": "/rest/api/space/FS"
            }
        },
        {
            "id": "393229",
            "type": "page",
            "status": "current",
            "title": "Page 1",
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/Page+1",
                "edit": "/pages/resumedraft.action?draftId=393229&draftShareId=f16d9e64-9373-4719-9df5-aec8102e5252",
                "tinyui": "/x/DQAG",
                "self": "http://localhost:8090/rest/api/content/393229"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393229/child",
                "restrictions": "/rest/api/content/393229/restriction/byOperation",
                "history": "/rest/api/content/393229/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393229/descendant",
                "space": "/rest/api/space/FS"
            }
        }
    ],
    "cursor": "content:false:null",
    "nextCursor": "content:false:393229",
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/rest/api/content/scan",
        "next": "/rest/api/content/scan?cursor=content:false:393229&limit=2",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}

## Browse content with pagination
To browse content with next or previous pagination use _links.next or _links.prev.


Copy
curl -u admin:admin http://localhost:8090/rest/api/content?limit=2&start=2 | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "393239",
            "type": "page",
            "status": "current",
            "title": "Page 3",
            "extensions": {
                "position": 2
            },
            "_links": {
                "webui": "/display/FS/Page+3",
                "edit": "/pages/resumedraft.action?draftId=393239&draftShareId=9041c7ee-064e-448e-a354-d2117661ec0c",
                "tinyui": "/x/FwAG",
                "self": "http://localhost:8090/rest/api/content/393239"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393239/child",
                "restrictions": "/rest/api/content/393239/restriction/byOperation",
                "history": "/rest/api/content/393239/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393239/descendant",
                "space": "/rest/api/space/FS"
            }
        },
        {
            "id": "393244",
            "type": "page",
            "status": "current",
            "title": "Second space Home",
            "extensions": {
                "position": "none"
            },
            "_links": {
                "webui": "/display/SS/Second+space+Home",
                "edit": "/pages/resumedraft.action?draftId=393244",
                "tinyui": "/x/HAAG",
                "self": "http://localhost:8090/rest/api/content/393244"
            },
            "_expandable": {
                "container": "/rest/api/space/SS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393244/child",
                "restrictions": "/rest/api/content/393244/restriction/byOperation",
                "history": "/rest/api/content/393244/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393244/descendant",
                "space": "/rest/api/space/SS"
            }
        }
    ],
    "start": 2,
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/rest/api/content",
        "next": "/rest/api/content?limit=2&start=4",
        "prev": "/rest/api/content?limit=2&start=0",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}

## Browse content with pagination
This example shows how you can browse content with pagination in Confluence 7.18 and later. The scan endpoint provides better performance, but can only be used to browse pages (not blogs), and doesn't support offset, title, or creationdate parameters.

To browse content with next or previous pagination you can still use _links.next or _links.prev, or you can use the value of nextCursor and prevCursor to set the cursor in the next request.

To navigate forward using the value of nextCursor from the previous example:

## Scan pages (Confluence 7.18 or later)

Copy
curl -u admin:admin http://localhost:8090/rest/api/content/scan?cursor=content:false:393229&limit=2 | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "393239",
            "type": "page",
            "status": "current",
            "title": "Page 3",
            "extensions": {
                "position": 2
            },
            "_links": {
                "webui": "/display/FS/Page+3",
                "edit": "/pages/resumedraft.action?draftId=393239&draftShareId=9041c7ee-064e-448e-a354-d2117661ec0c",
                "tinyui": "/x/FwAG",
                "self": "http://localhost:8090/rest/api/content/393239"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393239/child",
                "restrictions": "/rest/api/content/393239/restriction/byOperation",
                "history": "/rest/api/content/393239/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393239/descendant",
                "space": "/rest/api/space/FS"
            }
        },
        {
            "id": "393244",
            "type": "page",
            "status": "current",
            "title": "Second space Home",
            "extensions": {
                "position": "none"
            },
            "_links": {
                "webui": "/display/SS/Second+space+Home",
                "edit": "/pages/resumedraft.action?draftId=393244",
                "tinyui": "/x/HAAG",
                "self": "http://localhost:8090/rest/api/content/393244"
            },
            "_expandable": {
                "container": "/rest/api/space/SS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393244/child",
                "restrictions": "/rest/api/content/393244/restriction/byOperation",
                "history": "/rest/api/content/393244/history",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393244/descendant",
                "space": "/rest/api/space/SS"
            }
        }
    ],
    "cursor": "content:false:393229",
    "nextCursor": "content:false:393244",
    "prevCursor": "content:true:393239",
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/rest/api/content/scan?cursor=content:false:393229",
        "next": "/rest/api/content/scan?cursor=content:false:393244&limit=2",
        "prev": "/rest/api/content/scan?cursor=content:true:393239&limit=2",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}
Scan blogs (Confluence 8.3 or later)

Copy
curl -u admin:admin http://localhost:8090/rest/api/content/scan?spaceKey=TEST&type=blogpost&limit=2&expand=relevantViewRestrictions | python -mjson.tool
Example result:


Copy
{
  "results": [
    {
      "id": "5668868",
      "type": "blogpost",
      "status": "current",
      "title": "1 blog",
      "position": -1,
      "restrictions": {
        "_links": {
          "self": "http://localhost:8090/rest/api/content/5668868/restriction/byOperation"
        },
        "_expandable": {
          "read": "",
          "update": ""
        }
      },
      "_links": {
        "webui": "/spaces/TEST/blog/2024/09/23/5668868/1+blog",
        "edit": "/pages/resumedraft.action?draftId=5668868&draftShareId=75ccdec4-c508-4dda-9c2a-502aff2b2804",
        "tinyui": "/x/BIBW",
        "self": "http://localhost:8090/rest/api/content/5668868"
      },
      "_expandable": {
        "container": "/rest/api/space/TEST",
        "metadata": "",
        "operations": "",
        "children": "/rest/api/content/5668868/child",
        "history": "/rest/api/content/5668868/history",
        "ancestors": "",
        "body": "",
        "version": "",
        "descendants": "/rest/api/content/5668868/descendant",
        "space": "/rest/api/space/TEST"
      }
    },
    {
      "id": "5668870",
      "type": "blogpost",
      "status": "current",
      "title": "2 Blog",
      "position": -1,
      "restrictions": {
        "_links": {
          "self": "http://localhost:8090/rest/api/content/5668870/restriction/byOperation"
        },
        "_expandable": {
          "read": "",
          "update": ""
        }
      },
      "_links": {
        "webui": "/spaces/TEST/blog/2024/09/23/5668870/2+Blog",
        "edit": "/pages/resumedraft.action?draftId=5668870&draftShareId=37cb746e-98ad-4c36-9523-709d1ad2daeb",
        "tinyui": "/x/BoBW",
        "self": "http://localhost:8090/rest/api/content/5668870"
      },
      "_expandable": {
        "container": "/rest/api/space/TEST",
        "metadata": "",
        "operations": "",
        "children": "/rest/api/content/5668870/child",
        "history": "/rest/api/content/5668870/history",
        "ancestors": "",
        "body": "",
        "version": "",
        "descendants": "/rest/api/content/5668870/descendant",
        "space": "/rest/api/space/TEST"
      }
    }
  ],
  "cursor": "blogpost:false:null",
  "nextCursor": "content:false:5668870",
  "limit": 2,
  "size": 2,
  "_links": {
    "self": "http://localhost:8090/rest/api/content/scan?spaceKey=TEST&cursor=blogpost%3Afalse%3Anull&expand=restrictions",
    "next": "/rest/api/content/scan?spaceKey=TEST&cursor=content%3Afalse%3A5668870&expand=restrictions&limit=2",
    "base": "http://localhost:8090/confluence",
    "context": "/confluence"
  }
}
Scan comments (Confluence 8.3 or later)

Copy
curl -u admin:admin http://localhost:8090/rest/api/content/scan?type=comment&expand=space,body.storage | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "4325378",
            "type": "comment",
            "status": "current",
            "title": "Re: SNTest Home",
            "space": {
                "id": 2326529,
                "key": "SNTES",
                "name": "SNTest",
                "status": "current",
                "type": "global",
                "creator": {
                    "type": "known",
                    "username": "admin",
                    "userKey": "402880e4923163ec019231648dc20000",
                    "profilePicture": {
                        "path": "/wiki/images/icons/profilepics/default.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "A. D. Ministrator",
                    "_links": {
                        "self": "http://localhost:8090/rest/api/user?key=402880e4923163ec019231648dc20000"
                    },
                    "_expandable": {
                        "status": ""
                    }
                },
                "creationDate": "2024-10-09T11:51:59.233+11:00",
                "lastModifier": {
                    "type": "known",
                    "username": "admin",
                    "userKey": "402880e4923163ec019231648dc20000",
                    "profilePicture": {
                        "path": "/wiki/images/icons/profilepics/default.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "A. D. Ministrator",
                    "_links": {
                        "self": "http://localhost:8090/rest/api/user?key=402880e4923163ec019231648dc20000"
                    },
                    "_expandable": {
                        "status": ""
                    }
                },
                "lastModificationDate": "2024-10-09T11:51:59.233+11:00",
                "_links": {
                    "webui": "/spaces/SNTES/overview",
                    "self": "http://localhost:8090/rest/api/space/SNTES"
                },
                "_expandable": {
                    "metadata": "",
                    "icon": "",
                    "description": "",
                    "retentionPolicy": "",
                    "homepage": "/rest/api/content/2293762"
                }
            },
            "position": -1,
            "body": {
                "storage": {
                    "value": "<p>This is a test comment.<ac:link><ri:attachment ri:filename=\"Happy Birthday.png\" /></ac:link></p><p><br /></p><p><br /></p>",
                    "representation": "storage",
                    "_expandable": {
                        "content": "/rest/api/content/4325378"
                    }
                },
                "_expandable": {
                    "editor": "",
                    "view": "",
                    "export_view": "",
                    "styled_view": "",
                    "anonymous_export_view": ""
                }
            },
            "extensions": {
                "location": "footer",
                "_expandable": {
                    "resolution": ""
                }
            },
            "_links": {
                "webui": "/spaces/SNTES/pages/2293762/SNTest+Home?focusedCommentId=4325378#comment-4325378",
                "self": "http://localhost:8090/rest/api/content/4325378"
            },
            "_expandable": {
                "container": "/rest/api/content/2293762",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/4325378/child",
                "restrictions": "/rest/api/content/4325378/restriction/byOperation",
                "history": "/rest/api/content/4325378/history",
                "ancestors": "",
                "version": "",
                "descendants": "/rest/api/content/4325378/descendant"
            }
        },
        {
            "id": "4325379",
            "type": "comment",
            "status": "current",
            "title": "Re: SNTest Home",
            "space": {
                "id": 2326529,
                "key": "SNTES",
                "name": "SNTest",
                "status": "current",
                "type": "global",
                "creator": {
                    "type": "known",
                    "username": "admin",
                    "userKey": "402880e4923163ec019231648dc20000",
                    "profilePicture": {
                        "path": "/wiki/images/icons/profilepics/default.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "A. D. Ministrator",
                    "_links": {
                        "self": "http://localhost:8090/rest/api/user?key=402880e4923163ec019231648dc20000"
                    },
                    "_expandable": {
                        "status": ""
                    }
                },
                "creationDate": "2024-10-09T11:51:59.233+11:00",
                "lastModifier": {
                    "type": "known",
                    "username": "admin",
                    "userKey": "402880e4923163ec019231648dc20000",
                    "profilePicture": {
                        "path": "/wiki/images/icons/profilepics/default.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "A. D. Ministrator",
                    "_links": {
                        "self": "http://localhost:8090/rest/api/user?key=402880e4923163ec019231648dc20000"
                    },
                    "_expandable": {
                        "status": ""
                    }
                },
                "lastModificationDate": "2024-10-09T11:51:59.233+11:00",
                "_links": {
                    "webui": "/spaces/SNTES/overview",
                    "self": "http://localhost:8090/rest/api/space/SNTES"
                },
                "_expandable": {
                    "metadata": "",
                    "icon": "",
                    "description": "",
                    "retentionPolicy": "",
                    "homepage": "/rest/api/content/2293762"
                }
            },
            "position": -1,
            "body": {
                "storage": {
                    "value": "<p>Reply Comment.</p><table><colgroup><col /><col /></colgroup><tbody><tr><th scope=\"col\">Col1</th><th scope=\"col\">Col2</th></tr><tr><td>1</td><td>2</td></tr></tbody></table>",
                    "representation": "storage",
                    "_expandable": {
                        "content": "/rest/api/content/4325379"
                    }
                },
                "_expandable": {
                    "editor": "",
                    "view": "",
                    "export_view": "",
                    "styled_view": "",
                    "anonymous_export_view": ""
                }
            },
            "extensions": {
                "location": "footer",
                "_expandable": {
                    "resolution": ""
                }
            },
            "_links": {
                "webui": "/spaces/SNTES/pages/2293762/SNTest+Home?focusedCommentId=4325379#comment-4325379",
                "self": "http://localhost:8090/rest/api/content/4325379"
            },
            "_expandable": {
                "container": "/rest/api/content/2293762",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/4325379/child",
                "restrictions": "/rest/api/content/4325379/restriction/byOperation",
                "history": "/rest/api/content/4325379/history",
                "ancestors": "",
                "version": "",
                "descendants": "/rest/api/content/4325379/descendant"
            }
        }
    ],
    "cursor": "comment:false:null",
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/confluenceapi/content/scan?cursor=comment%3Afalse%3Anull&expand=space%2Cbody.storage",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}

## Read content, and expand the body
This example shows how you can read content of a page with the body expanded.


Copy
curl -u admin:admin http://localhost:8090/rest/api/content/3965072?expand=body.storage |
python -mjson.tool
Example result:


Copy
{
    "_expandable": {
        "ancestors": "",
        "children": "",
        "container": "",
        "history": "/rest/api/content/3965072/history",
        "metadata": "",
        "space": "/rest/api/space/TST",
        "version": ""
    },
    "_links": {
        "base": "http://localhost:8090/confluence",
        "collection": "/rest/api/contents",
        "self": "http://localhost:8090/rest/api/content/3965072",
        "tinyui": "/x/kIA8",
        "webui": "/display/TST/Test+Page"
    },
    "body": {
        "editor": {
            "_expandable": {
                "content": "/rest/api/content/3965072"
            },
            "representation": "editor"
        },
        "export_view": {
            "_expandable": {
                "content": "/rest/api/content/3965072"
            },
            "representation": "export_view"
        },
        "storage": {
            "_expandable": {
                "content": "/rest/api/content/3965072"
            },
            "representation": "storage",
            "value": "<p>blah blah</p>"
        },
        "view": {
            "_expandable": {
                "content": "/rest/api/content/3965072"
            },
            "representation": "view"
        }
    },
    "id": "3965072",
    "title": "Test Page",
    "type": "page"
}

## Find pages or blogs

## Find pages by space key (Confluence 7.18 or later)
This example shows how you can find pages in Confluence 7.18 and later. The scan endpoint provides better performance, but can only be used to browse pages (not blogs), and doesn't support offset, title, or creationdate parameters.

This example shows how you can find a page by space key, with history expanded to find the creator.


Copy
curl -u admin:admin http://localhost:8090/rest/api/content/scan?spaceKey=FS&limit=2&expand=history | python -mjson.tool
Example result:


Copy
{
    "results": [
        {
            "id": "393219",
            "type": "page",
            "status": "current",
            "title": "First space",
            "history": {
                "latest": true,
                "createdBy": {
                    "type": "anonymous",
                    "profilePicture": {
                        "path": "/confluence/s/-ze4av5/8804/0/_/images/icons/profilepics/anonymous.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "Anonymous"
                },
                "createdDate": "2022-04-27T07:15:13.012+10:00",
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/393219/history"
                },
                "_expandable": {
                    "lastUpdated": "",
                    "previousVersion": "",
                    "contributors": "",
                    "nextVersion": ""
                }
            },
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/First+space",
                "edit": "/pages/resumedraft.action?draftId=393219",
                "tinyui": "/x/AwAG",
                "self": "http://localhost:8090/rest/api/content/393219"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393219/child",
                "restrictions": "/rest/api/content/393219/restriction/byOperation",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393219/descendant",
                "space": "/rest/api/space/FS"
            }
        },
        {
            "id": "393229",
            "type": "page",
            "status": "current",
            "title": "Page 1",
            "history": {
                "latest": true,
                "createdBy": {
                    "type": "known",
                    "username": "admin",
                    "userKey": "2c9d802a8067b72f018067b876420000",
                    "profilePicture": {
                        "path": "/confluence/images/icons/profilepics/default.svg",
                        "width": 48,
                        "height": 48,
                        "isDefault": true
                    },
                    "displayName": "admin",
                    "_links": {
                        "self": "http://localhost:8090/rest/api/user?key=2c9d802a8067b72f018067b876420000"
                    },
                    "_expandable": {
                        "status": ""
                    }
                },
                "createdDate": "2022-04-27T07:15:18.097+10:00",
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/393229/history"
                },
                "_expandable": {
                    "lastUpdated": "",
                    "previousVersion": "",
                    "contributors": "",
                    "nextVersion": ""
                }
            },
            "extensions": {
                "position": 0
            },
            "_links": {
                "webui": "/display/FS/Page+1",
                "edit": "/pages/resumedraft.action?draftId=393229&draftShareId=f16d9e64-9373-4719-9df5-aec8102e5252",
                "tinyui": "/x/DQAG",
                "self": "http://localhost:8090/rest/api/content/393229"
            },
            "_expandable": {
                "container": "/rest/api/space/FS",
                "metadata": "",
                "operations": "",
                "children": "/rest/api/content/393229/child",
                "restrictions": "/rest/api/content/393229/restriction/byOperation",
                "ancestors": "",
                "body": "",
                "version": "",
                "descendants": "/rest/api/content/393229/descendant",
                "space": "/rest/api/space/FS"
            }
        }
    ],
    "cursor": "content:false:null",
    "nextCursor": "content:false:393229",
    "limit": 2,
    "size": 2,
    "_links": {
        "self": "http://localhost:8090/rest/api/content/scan?spaceKey=FS&expand=history",
        "next": "/rest/api/content/scan?spaceKey=FS&cursor=content:false:393229&expand=history&limit=2",
        "base": "http://localhost:8090/confluence",
        "context": "/confluence"
    }
}

## Find a page by title and space key
This example shows how you can find a page by space key and title with history expanded to find the creator.


Copy
curl -u admin:admin -X GET "http://localhost:8090/rest/api/content?title=myPage%20Title
&spaceKey=TST&expand=history" | python -mjson.tool
Example result:


Copy
{
    "_links": {
        "self": "http://localhost:8090/rest/api/content"
    },
    "limit": 100,
    "results": [
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/950276/child",
                "container": "",
                "descendants": "/rest/api/content/950276/descendant",
                "metadata": "",
                "space": "/rest/api/space/TST",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8090/rest/api/content/950276",
                "tinyui": "/x/BIAO",
                "webui": "/display/TST/myPage+Title"
            },
            "history": {
                "_expandable": {
                    "lastUpdated": ""
                },
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/950276/history"
                },
                "createdBy": {
                    "displayName": "A. D. Ministrator",
                    "profilePicture": {
                        "height": 48,
                        "isDefault": true,
                        "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                        "width": 48
                    },
                    "type": "known",
                    "username": "admin"
                },
                "createdDate": "2014-03-07T17:08:20.326+1100",
                "latest": true
            },
            "id": "950276",
            "title": "myPage Title",
            "type": "page"
        }
    ],
    "size": 1,
    "start": 0
}
Find blog posts
This example finds blog posts to display in a blog roll with labels.


Copy
curl -u admin:admin -X GET "http://localhost:8090/rest/api/content?type=blogpost&start=0
&limit=10&expand=space,history,body.view,metadata.labels" | python -mjson.tool
Example result:


Copy
{
    "_links": {
        "self": "http://localhost:8090/rest/api/content"
    },
    "limit": 10,
    "results": [
        {
            "_expandable": {
                "ancestors": "",
                "children": "/rest/api/content/557065/child",
                "container": "",
                "descendants": "/rest/api/content/557065/descendant",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8090/rest/api/content/557065",
                "tinyui": "/x/CYAI",
                "webui": "/display/TST/Test+Space+Home"
            },
            "body": {
                "editor": {
                    "_expandable": {
                        "content": "/rest/api/content/557065"
                    },
                    "representation": "editor"
                },
                "export_view": {
                    "_expandable": {
                        "content": "/rest/api/content/557065"
                    },
                    "representation": "export_view"
                },
                "storage": {
                    "_expandable": {
                        "content": "/rest/api/content/557065"
                    },
                    "representation": "storage"
                },
                "view": {
                    "_expandable": {
                        "content": "/rest/api/content/557065"
                    },
                    "representation": "view",
                    "value": "<p>Example page</p>"
                }
            },
            "history": {
                "_expandable": {
                    "lastUpdated": ""
                },
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/557065/history"
                },
                "createdBy": {
                    "displayName": "A. D. Ministrator",
                    "profilePicture": {
                        "height": 48,
                        "isDefault": true,
                        "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                        "width": 48
                    },
                    "type": "known",
                    "username": "admin"
                },
                "createdDate": "2014-03-07T16:14:35.220+1100",
                "latest": true
            },
            "id": "557065",
            "metadata": {
                "labels": {
                    "_links": {
                        "self": "http://localhost:8090/rest/api/content/557065/label"
                    },
                    "limit": 200,
                    "results": [],
                    "size": 0,
                    "start": 0
                },
                "likesCount": null
            },
            "space": {
                "_links": {
                    "self": "http://localhost:8090/rest/api/space/TST"
                },
                "id": 786433,
                "key": "TST",
                "name": "Test Space"
            },
            "title": "Test Space Home",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "children": "/rest/api/content/557067/child",
                "container": "",
                "descendants": "/rest/api/content/557067/descendant",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8090/rest/api/content/557067",
                "tinyui": "/x/C4AI",
                "webui": "/display/TST/A+new+page"
            },
            "body": {
                "editor": {
                    "_expandable": {
                        "content": "/rest/api/content/557067"
                    },
                    "representation": "editor"
                },
                "export_view": {
                    "_expandable": {
                        "content": "/rest/api/content/557067"
                    },
                    "representation": "export_view"
                },
                "storage": {
                    "_expandable": {
                        "content": "/rest/api/content/557067"
                    },
                    "representation": "storage"
                },
                "view": {
                    "_expandable": {
                        "content": "/rest/api/content/557067"
                    },
                    "representation": "view",
                    "value": ""
                }
            },
            "history": {
                "_expandable": {
                    "lastUpdated": ""
                },
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/557067/history"
                },
                "createdBy": {
                    "displayName": "A. D. Ministrator",
                    "profilePicture": {
                        "height": 48,
                        "isDefault": true,
                        "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                        "width": 48
                    },
                    "type": "known",
                    "username": "admin"
                },
                "createdDate": "2014-03-07T16:18:33.554+1100",
                "latest": true
            },
            "id": "557067",
            "metadata": {
                "labels": {
                    "_links": {
                        "self": "http://localhost:8090/rest/api/content/557067/label"
                    },
                    "limit": 200,
                    "results": [],
                    "size": 0,
                    "start": 0
                },
                "likesCount": null
            },
            "space": {
                "_links": {
                    "self": "http://localhost:8090/rest/api/space/TST"
                },
                "id": 786433,
                "key": "TST",
                "name": "Test Space"
            },
            "title": "A new page",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "children": "/rest/api/content/950276/child",
                "container": "",
                "descendants": "/rest/api/content/950276/descendant",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8090/rest/api/content/950276",
                "tinyui": "/x/BIAO",
                "webui": "/display/TST/myPage+Title"
            },
            "body": {
                "editor": {
                    "_expandable": {
                        "content": "/rest/api/content/950276"
                    },
                    "representation": "editor"
                },
                "export_view": {
                    "_expandable": {
                        "content": "/rest/api/content/950276"
                    },
                    "representation": "export_view"
                },
                "storage": {
                    "_expandable": {
                        "content": "/rest/api/content/950276"
                    },
                    "representation": "storage"
                },
                "view": {
                    "_expandable": {
                        "content": "/rest/api/content/950276"
                    },
                    "representation": "view",
                    "value": "<p>Some content</p>"
                }
            },
            "history": {
                "_expandable": {
                    "lastUpdated": ""
                },
                "_links": {
                    "self": "http://localhost:8090/rest/api/content/950276/history"
                },
                "createdBy": {
                    "displayName": "A. D. Ministrator",
                    "profilePicture": {
                        "height": 48,
                        "isDefault": true,
                        "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                        "width": 48
                    },
                    "type": "known",
                    "username": "admin"
                },
                "createdDate": "2014-03-07T17:08:20.326+1100",
                "latest": true
            },
            "id": "950276",
            "metadata": {
                "labels": {
                    "_links": {
                        "self": "http://localhost:8090/rest/api/content/950276/label"
                    },
                    "limit": 200,
                    "results": [],
                    "size": 0,
                    "start": 0
                },
                "likesCount": null
            },
            "space": {
                "_links": {
                    "self": "http://localhost:8090/rest/api/space/TST"
                },
                "id": 786433,
                "key": "TST",
                "name": "Test Space"
            },
            "title": "myPage Title",
            "type": "page"
        }
    ],
    "size": 3,
    "start": 0
}

## Create a new page
This example shows how you can create a new page with content in a specific space.


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d '{"type":"page","title":"new page",
"space":{"key":"TST"},"body":{"storage":{"value":"<p>This is <br/> a new page</p>","representation":
"storage"}}}' http://localhost:8090/rest/api/content/ | python -mjson.tool
Example result:


Copy
{
    "_expandable": {
        "children": "/rest/api/content/3604482/child",
        "descendants": "/rest/api/content/3604482/descendant",
        "metadata": ""
    },
    "_links": {
        "base": "http://localhost:8090/confluence",
        "collection": "/rest/api/contents",
        "self": "http://localhost:8090/rest/api/content/3604482",
        "tinyui": "/x/AgA3",
        "webui": "/display/TST/new+page"
    },
    "ancestors": [],
    "body": {
        "editor": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "editor"
        },
        "export_view": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "export_view"
        },
        "storage": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "storage",
            "value": "<p>This is a new page</p>"
        },
        "view": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "view"
        }
    },
    "container": {
        "_links": {
            "self": "http://localhost:8090/rest/api/space/TST"
        },
        "id": 2719747,
        "key": "TST",
        "name": "Test Space"
    },
    "history": {
        "_expandable": {
            "lastUpdated": ""
        },
        "_links": {
            "self": "http://localhost:8090/rest/api/content/3604482/history"
        },
        "createdBy": {
            "displayName": "A. D. Ministrator",
            "profilePicture": {
                "height": 48,
                "isDefault": true,
                "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                "width": 48
            },
            "type": "known",
            "username": "admin"
        },
        "createdDate": "2014-03-10T23:14:35.031+1100",
        "latest": true
    },
    "id": "3604482",
    "space": {
        "_links": {
            "self": "http://localhost:8090/rest/api/space/TST"
        },
        "id": 2719747,
        "key": "TST",
        "name": "Test Space"
    },
    "title": "new page",
    "type": "page",
    "version": {
        "by": {
            "displayName": "A. D. Ministrator",
            "profilePicture": {
                "height": 48,
                "isDefault": true,
                "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                "width": 48
            },
            "type": "known",
            "username": "admin"
        },
        "message": "",
        "minorEdit": false,
        "number": 1,
        "when": "2014-03-10T23:14:35.031+1100"
    }
}
Create a new page (jQuery)

Copy
//This creates a page in a space.
var username = "admin";
var password = "admin";
var jsondata = {"type":"page",
 "title":"My Test Page",
 "space":{"key":"TST"},
 "body":{"storage":{"value":"<p>This is a new page</p>","representation":"storage"}}};

$.ajax
  ({
    type: "POST",
    url: "http://localhost:8090/rest/api/content/",
    contentType:"application/json; charset=utf-8",
    dataType: "json",
    async: false,
    headers: {
        "Authorization": "Basic " + btoa(username+ ":" + password)
    },
    data: JSON.stringify(jsondata),
    success: function (){
        console.log('Page saved!');
    },
    error : function(xhr, errorText){
        console.log('Error '+ xhr.responseText);
    }
});

## Create a new page as a child of another page
This example shows how you can create a new page, with content, as a child of another page with ID 456


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d '{"type":"page","title":"new page",
"ancestors":[{"id":456}], "space":{"key":"TST"},"body":{"storage":{"value":
"<p>This is a new page</p>","representation":"storage"}}}'
http://localhost:8090/rest/api/content/ | python -mjson.tool
Update a page
This example shows how you can update the content of an existing page. 


Copy
curl -u admin:admin -X PUT -H 'Content-Type: application/json' -d '{"id":"3604482","type":"page",
"title":"new page","space":{"key":"TST"},"body":{"storage":{"value":
"<p>This is the updated text for the new page</p>","representation":"storage"}},
"version":{"number":2}}' http://localhost:8090/rest/api/content/3604482 | python -mjson.tool
Example result:


Copy
{
    "_expandable": {
        "children": "/rest/api/content/3604482/child",
        "descendants": "/rest/api/content/3604482/descendant",
        "metadata": ""
    },
    "_links": {
        "base": "http://localhost:8090/confluence",
        "collection": "/rest/api/contents",
        "self": "http://localhost:8090/rest/api/content/3604482",
        "tinyui": "/x/AgA3",
        "webui": "/display/TST/new+page"
    },
    "ancestors": [],
    "body": {
        "editor": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "editor"
        },
        "export_view": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "export_view"
        },
        "storage": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "storage",
            "value": "<p>This is the updated text for the new page</p>"
        },
        "view": {
            "_expandable": {
                "content": "/rest/api/content/3604482"
            },
            "representation": "view"
        }
    },
    "container": {
        "_links": {
            "self": "http://localhost:8090/rest/api/space/TST"
        },
        "id": 2719747,
        "key": "TST",
        "name": "Test Space"
    },
    "history": {
        "_expandable": {
            "lastUpdated": "",
            "previousVersion": ""
        },
        "_links": {
            "self": "http://localhost:8090/rest/api/content/3604482/history"
        },
        "createdBy": {
            "displayName": "A. D. Ministrator",
            "profilePicture": {
                "height": 48,
                "isDefault": true,
                "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                "width": 48
            },
            "type": "known",
            "username": "admin"
        },
        "createdDate": "2014-03-10T23:14:35.031+1100",
        "latest": true
    },
    "id": "3604482",
    "space": {
        "_links": {
            "self": "http://localhost:8090/rest/api/space/TST"
        },
        "id": 2719747,
        "key": "TST",
        "name": "Test Space"
    },
    "title": "new page",
    "type": "page",
    "version": {
        "by": {
            "displayName": "A. D. Ministrator",
            "profilePicture": {
                "height": 48,
                "isDefault": true,
                "path": "/confluence/s/en_GB-1988229788/4960/NOCACHE1/_/images/icons/profilepics/default.png",
                "width": 48
            },
            "type": "known",
            "username": "admin"
        },
        "minorEdit": false,
        "number": 2,
        "when": "2014-03-10T23:16:50.757+1100"
    }
}

## Delete a page
This example shows how you can delete a page by content ID.


Copy
curl -v -S -u admin:admin -X DELETE http://localhost:8090/rest/api/content/3604482 | python -mjson.tool
Expect a HTTP/1.1 204 No Content response after a successful deletion.

## Upload an attachment
This example shows how you can upload an attachment to a specific page (where 3604482 is the content ID), and add a comment.


Copy
curl -v -S -u admin:admin -X POST -H "X-Atlassian-Token: no-check" -F "file=@myfile.txt" -F
"comment=this is my file" "http://localhost:8090/rest/api/content/3604482/child/attachment"
| python -mjson.tool

Copy
{
    "_expandable": {
        "icon": ""
    },
    "_links": {
        "base": "http://localhost:8090/confluence",
        "collection": "/rest/api/space",
        "context": "/confluence",
        "self": "http://localhost:8090/rest/api/space/RAID4"
    },
    "description": {
        "_expandable": {
            "view": ""
        },
        "plain": {
            "representation": "plain",
            "value": "Raider Space for raiders"
        }
    },
    "homepage": {
        "_expandable": {
            "ancestors": "",
            "body": "",
            "children": "/rest/api/content/3997704/child",
            "container": "",
            "descendants": "/rest/api/content/3997704/descendant",
            "history": "/rest/api/content/3997704/history",
            "metadata": "",
            "space": "/rest/api/space/RAID4",
            "version": ""
        },
        "_links": {
            "self": "http://localhost:8090/rest/api/content/3997704",
            "tinyui": "/x/CAA9",
            "webui": "/display/RAID4/Raider+Home"
        },
        "id": "3997704",
        "title": "Raider Home",
        "type": "page"
    },
    "id": 4030468,
    "key": "RAID",
    "name": "Raider",
    "type": "global"
}
Download an attachment
This example shows how you can download an attachment from a specific page (where 1998856 is the content ID).


Copy
curl -u admin:admin "http://localhost:8090/rest/api/content/1998856/child/attachment" | python -m json.tool
The download link is inside output:


Copy
"_links": {
    "download": "/download/attachments/1998856/test.txt?version=1&modificationDate=1519985997040&api=v2",
    "self": "http://localhost:8090/rest/api/content/att1998865",
    "webui":"/display/dsada/new4+page?preview=%2F1998856%2F1998865%2Ftest.txt"
}
Get comments from a page

Copy
curl -u admin:admin "http://localhost:8090/rest/api/content/1998856/child/comment?expand=body.view&depth=all" | python -m json.tool

Copy
{
    "_links": {
        "base": "http://localhost:8090/confluence",
        "context": "/confluence",
        "self": "http://localhost:8090/rest/api/content/1998856/child/comment?expand=body.view"
    },
    "limit": 25,
    "results": [
        {
            "_expandable": {
                "ancestors": "",
                "children": "/rest/api/content/1998866/child",
                "container": "/rest/api/content/1998856",
                "descendants": "/rest/api/content/1998866/descendant",
                "history": "/rest/api/content/1998866/history",
                "metadata": "",
                "operations": "",
                "restrictions": "/rest/api/content/1998866/restriction/byOperation",
                "space": "/rest/api/space/dsada",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8090/rest/api/content/1998866",
                "webui": "/display/dsada/new4+page?focusedCommentId=1998866#comment-1998866"
            },
            "body": {
                "_expandable": {
                    "anonymous_export_view": "",
                    "editor": "",
                    "export_view": "",
                    "storage": "",
                    "styled_view": ""
                },
                "view": {
                    "_expandable": {
                        "content": "/rest/api/content/1998866",
                        "webresource": ""
                    },
                    "representation": "storage",
                    "value": "<p><strong>I am a comment</strong></p>"
                }
            },
            "extensions": {
                "_expandable": {
                    "resolution": ""
                },
                "location": "footer"
            },
            "id": "1998866",
            "status": "current",
            "title": "Re: new4 page",
            "type": "comment"
        }
    ],
    "size": 1,
    "start": 0
}
Add a comment to a page (Python)
This Python example shows how you can add a comment to a page. First, the page for commenting is fetched from API by title, and then used as the container of the comment.

comment.py


Copy
import requests, json
def printResponse(r):
    print '{} {}\n'.format(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')), r)
r = requests.get('http://localhost:8090/rest/api/content',
    params={'title' : 'Page title to comment on'},
    auth=('admin', 'admin'))
printResponse(r)
parentPage = r.json()['results'][0]
pageData = {'type':'comment', 'container':parentPage,
    'body':{'storage':{'value':"<p>A new comment</p>",'representation':'storage'}}}
r = requests.post('http://localhost:8090/rest/api/content',
    data=json.dumps(pageData),
    auth=('admin','admin'),
    headers=({'Content-Type':'application/json'}))
printResponse(r)
Create a page with a task 
This examples is similar to creating a page but you need to use the following JSON body, see Confluence Storage Format documenation for other storage format markup that you can use.


Copy
POST /rest/api/content :

{
  "type":"page",
  "title":"Another planning specs with username",
  "body":{ "storage":{"value":
        "<ac:task-list>
           <ac:task>
             <ac:task-status>incomplete</ac:task-status>
             <ac:task-body>
               <ac:link><ri:user ri:username='admin' /></ac:link>
               do something
             </ac:task-body>
            </ac:task>
          </ac:task-list>",
      "representation":"storage"}},
  "space":{"key":"TST"}
}
Create a space
This example shows how you can create a new space.


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d' { "key":"RAID", "name":"Raider",
"type":"global",  "description":{"plain": { "value": "Raider Space for raiders","representation":
"plain" }}}' http://localhost:8090/rest/api/space
Converting content
Convert storage format to view format
This example shows how to convert storage format to view format.


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d'{"value":"<ac:structured-macro
ac:name=\"cheese\" />","representation":"storage"}'
"http://localhost:8090/rest/api/contentbody/convert/view" | python -mjson.tool
Example result:


Copy
{
    "_links": {
        "base": "http://localhost:8090/confluence"
    },
    "representation": "view",
    "value": "I like cheese!"
}
Convert wiki markup to storage format
This example shows how to convert wiki markup to storage format.


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d'{"value":"{cheese}",
"representation":"wiki"}' "http://localhost:8090/rest/api/contentbody/convert/storage"
| python -mjson.tool
Example result:


Copy
{
    "_links": {
        "base": "http://localhost:8090/confluence"
    },
    "representation": "storage",
    "value": "<ac:structured-macro ac:name=\"cheese\" />"
}
Convert storage format to view using a particular page for the conversion context
This example also shows how to convert storage format to view format, but this time using an existing piece of content for the conversion context. Some macros require a page context when they are executed. I'm using the space attachments macro. To determine what attachments to show on the page, this macro uses the space that the page is in.


Copy
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d'{"representation":"storage",
"value":"<p><ac:structured-macro ac:name=\"space-attachments\"/></p>","content":{"id":"1448805348"}}'
"http://localhost:8090/rest/api/contentbody/convert/view" | python -mjson.tool