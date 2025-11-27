import QtQuick
import QtQuick.Controls

Page {
    title: "Reader view"

    Rectangle {
        anchors.fill: parent
        color: "#e0f7fa" // Light cyan background to tell them apart

        Column {
            anchors.centerIn: parent
            spacing: 20

            
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