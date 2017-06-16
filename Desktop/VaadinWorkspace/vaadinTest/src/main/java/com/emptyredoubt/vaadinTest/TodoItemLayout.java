package com.emptyredoubt.vaadinTest;

import com.vaadin.data.Binder;
import com.vaadin.ui.*;
import com.vaadin.ui.Component;
import com.vaadin.ui.CheckBox;
import com.vaadin.ui.TextField;
import com.vaadin.ui.themes.ValoTheme;

/**
 * Created by theuser on 6/16/2017.
 */

public class TodoItemLayout extends HorizontalLayout {
    private final CheckBox done;
    private final TextField text;

    public TodoItemLayout(Todo todo, TodoChangeListener changeListener) {
        setWidth("100%");
        setDefaultComponentAlignment(Alignment.MIDDLE_LEFT);
        done = new CheckBox();
        text = new TextField();
        text.addStyleName(ValoTheme.TEXTFIELD_BORDERLESS);

        Binder<Todo> binder = new Binder<>(Todo.class);
        binder.bindInstanceFields(this);
        binder.setBean(todo);

        addComponent(done);
        addComponentsAndExpand(text);

        binder.addValueChangeListener(event -> changeListener.TodoChanged(todo));
    }
}
