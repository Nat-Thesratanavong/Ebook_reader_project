import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Ebook Reader"

    // The StackView manages the pages
    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: mainMenuPage 
    }

    // Define the Main Menu Page here
    Component {
        id: mainMenuPage

        Page {
            Rectangle {
                anchors.fill: parent
                color: "#f0f0f0"

                Column {
                    anchors.centerIn: parent
                    spacing: 20

                    Text {
                        text: "Main Menu"
                        font.pixelSize: 24
                        font.bold: true
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    // The Button to switch views
                    Button {
                        text: "Go to Second Screen"
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: {
                            // Push the distinct QML file onto the stack
                            stackView.push("second_window.qml")
                        }
                    }

                    Button {
                        text: "Go to Reader view"
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: {
                            stackView.push("reader_view.qml")
                        }
                    }
                }
            }
        }
    }
}