package com.emptyredoubt.vaadinTest;

import com.vaadin.annotations.Theme;
import com.vaadin.event.ShortcutAction;
import com.vaadin.icons.VaadinIcons;
import com.vaadin.server.VaadinRequest;
import com.vaadin.spring.annotation.SpringUI;
import com.vaadin.ui.*;
import com.vaadin.ui.themes.ValoTheme;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * Created by emptyRedoubt on 6/15/2017.
 */
@SpringUI
@Theme("valo")
public class TodoUI extends UI {
    private VerticalLayout root;

    @Autowired
    TodoLayout todoLayout;

    @Override
    protected void init(VaadinRequest vaadinRequest) {
        setupLayout();
        addHeader();
        addForm();
        addTodoList();
        addDeleteButton();
        
    }

    private void addTodoList() {
        todoLayout.setWidth("80%");
        root.addComponent(todoLayout);
    }

    private void addForm() {
        HorizontalLayout formLayout = new HorizontalLayout();
        TextField task = new TextField();
        Button add = new Button("");
        add.addStyleName(ValoTheme.BUTTON_FRIENDLY);
        add.setIcon(VaadinIcons.PLUS);
        formLayout.setWidth("80%");
        formLayout.addComponentsAndExpand(task);
        formLayout.addComponents(add);
        add.addClickListener(clickEvent -> {
                    todoLayout.addTodo(new Todo(task.getValue()));
                    task.clear();
                    task.focus();
                });
        task.focus();
        add.setClickShortcut(ShortcutAction.KeyCode.ENTER);
        root.addComponent(formLayout);
    }

    private void addHeader() {
        Label header = new Label( "To Do List");
        header.addStyleName(ValoTheme.LABEL_H1);
        root.addComponent(header);
    }

    private void setupLayout() {
        root = new VerticalLayout();
        root.setDefaultComponentAlignment(Alignment.MIDDLE_CENTER);
        setContent(root);
    }

    private void addDeleteButton() {
        root.addComponent(new Button ("Click to delete", click -> {
            todoLayout.deleteCompleted();
        }));
    }
}
