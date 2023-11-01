# Presentations

A Presentation is the an output of TADAA that represents a client-deliverable. This is currently only in the form of a PowerPoint.

What data is used, how it is used, and how it will ask the analyst for this data is defined in a `presentation.json` file.

*ppts/json/presentation.json*

Types:
- text
- boolean
- link
- image
- number
- data
- delete

```
schema = {
  "name": "original",
  "ppt": "SEOC Tech Audit Template.pptx",
  "target_export_files": [],
  slides= [
    {
      "index": 0,
      "name": "",
      "shapes": [
        {
          "key": "",
          "type": "",
          "input": {
            "label": "",
            "options": [
              {
                "label": "",
                "value": ""
              }
            ]
          }
        }
      ]
    }
  ]
}
```