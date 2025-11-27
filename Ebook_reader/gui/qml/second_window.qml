import QtQuick
import QtQuick.Controls

Page {
    title: "Second Screen"

    Rectangle {
        anchors.fill: parent
        color: "#e0f7fa" // Light cyan background to tell them apart

        Column {
            anchors.centerIn: parent
            spacing: 20

            Text {
                text: "Second Screen"
                font.pixelSize: 24
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Button {
                text: "Click Me (Test Backend)"
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: {
                    // Call the new Python backend
                    secondBackend.do_something()
                }
            }

            Button {
                text: "Go Back"
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: {
                    // Pop this view off the stack (return to Main Menu)
                    stackView.pop()
                }
            }
        }
    }
}